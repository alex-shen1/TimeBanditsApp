"""Views related to tasks."""""
# pylint: disable=too-many-ancestors,invalid-name
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import stripe

from ..models import Task
from ..forms.task_form import TaskForm


# don't really know what kind of view from generic should be used
class TasksView(generic.ListView):
    """Lists all available Tasks."""
    # shouldn't the map be part of this view?
    template_name = 'tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()


# class CreateTasksView(generic.TemplateView):
#     """Form where user can create a Task."""
#     template_name = 'tasks/create_task.html'
#     model = Task
def create_task(request):
    """Creates a Task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            if form.cleaned_data['donation_amount'] > 0:
                return render(request, 'tasks/checkout.html',
                              {'form': form, 'amount': form.cleaned_data['donation_amount']})
            return HttpResponseRedirect('/tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


def update_task(request, pk):
    """Updates a Task."""
    # reference:
    # http://www.learningaboutelectronics.com/Articles/How-to-create-an-update-view-with-a-Django-form-in-Django.php
    obj = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=obj)
    context = {'form': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form': form}
        # return render(request, 'tasks/update_task.html', context)
        return HttpResponseRedirect("/tasks")
    context = {'form': form, 'pk': pk}
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


class TaskDetailsView(generic.DetailView):
    """Displays details for a particular Task."""
    template_name = 'tasks/task_details.html'
    model = Task
