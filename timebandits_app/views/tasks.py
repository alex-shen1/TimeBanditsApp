"""Views related to tasks."""""
# pylint: disable=too-many-ancestors,invalid-name
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

import stripe
import django_filters
from django_filters.views import FilterView

from ..models import Task
from ..forms.task_form import TaskForm


class TaskFilter(django_filters.FilterSet):
    """Filters Tasks for displaying in template"""
    # reference:
    # https://django-filter.readthedocs.io/en/latest/guide/usage.html
    # https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
    task_title = django_filters.CharFilter(lookup_expr='icontains')
    task_description = django_filters.CharFilter(lookup_expr='icontains')
    event_date = django_filters.NumberFilter(
        field_name='event_date', lookup_expr='year')

    # time_to_complete = django_filters.NumberFilter()

    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'event_date']


class TasksView(FilterView):
    """Lists all available Tasks."""
    template_name = 'tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter


# class CreateTasksView(generic.TemplateView):
#     """Form where user can create a Task."""
#     template_name = 'tasks/create_task.html'
#     model = Task

@login_required
def create_task(request):
    """Creates a Task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user.account
            task.save()

            if form.cleaned_data['donation_amount'] > 0:
                return render(request, 'tasks/checkout.html',
                              {'form': form, 'amount': form.cleaned_data['donation_amount']})
            return HttpResponseRedirect('/tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def update_task(request, pk):
    """Updates a Task."""
    # reference:
    # http://www.learningaboutelectronics.com/Articles/How-to-create-an-update-view-with-a-Django-form-in-Django.php
    task = Task.objects.get(id=pk)
    task_owner = task.owner
    if task_owner != request.user.account:
        return HttpResponseRedirect("/tasks")
    obj = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/tasks")
    context = {'form': form, 'taskid': pk}
    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    """Deletes a Task."""
    obj = get_object_or_404(Task, id=pk)
    obj.delete()
    return HttpResponseRedirect('/tasks')


def charge(request):
    """Pays the donation amount of a task"""
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.Charge.create(
            amount=int(float(request.POST.get("amount", "")) * 100),
            currency='usd',
            description='Donations are mandatory, refunds are optional',
            source=request.POST['stripeToken']
        )
    # should redirect to /tasks even if no POST so it doesn't crash if
    # you manually attempt to go to /tasks/charge
    return HttpResponseRedirect('/tasks')


@login_required
def join_task(request, pk):
    """Adds a volunteer to a task"""
    # Increments num_volunteers by 1
    # Adds account to task's registered_accounts field
    task_to_join = Task.objects.get(id=pk)
    user = request.user
    task_to_join.num_volunteers = task_to_join.num_volunteers + 1
    task_to_join.registered_accounts.add(user.account)
    task_to_join.save()
    user.account.total_hours += task_to_join.time_to_complete
    user.account.save()
    return HttpResponseRedirect(f'/tasks/{pk}')


class TaskDetailsView(generic.DetailView):
    """Displays details for a particular Task."""
    template_name = 'tasks/task_details.html'
    model = Task


def search(request):
    """View for filtered task - not actually search"""
    task_list = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=task_list)
    return render(request, 'tasks/task_list.html', {'filter': task_filter})
