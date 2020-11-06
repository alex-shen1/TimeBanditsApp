"""Views related to tasks."""""
# pylint: disable=too-many-ancestors,invalid-name
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
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
    event_date = django_filters.NumberFilter(
        field_name='event_date', lookup_expr='year')
    time_to_complete = django_filters.NumberFilter()

    class Meta:
        model = Task
        fields = ['task_title', 'event_date', 'time_to_complete']


# don't really know what kind of view from generic should be used


class TasksView(FilterView):
    """Lists all available Tasks."""
    # shouldn't the map be part of this view?
    template_name = 'tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'
    filterset_class = TaskFilter


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


def join_task(request, pk):
    """Adds a volunteer to a task"""
    # Increments num_volunteers by 1
    # Adds account to task's registered_accounts field
    task_to_join = Task.objects.get(id=pk)
    task_to_join.num_volunteers = task_to_join.num_volunteers + 1
    task_to_join.registered_accounts.add(request.user.account)
    return HttpResponseRedirect('/tasks')


class TaskDetailsView(generic.DetailView):
    """Displays details for a particular Task."""
    template_name = 'tasks/task_details.html'
    model = Task


class TaskFilter(django_filters.FilterSet):
    """Filters Tasks for displaying in template"""
    # reference:
    # https://django-filter.readthedocs.io/en/latest/guide/usage.html
    # https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
    task_title = django_filters.CharFilter(lookup_expr='icontains')
    event_date = django_filters.NumberFilter(
        field_name='event_date', lookup_expr='year')
    time_to_complete = django_filters.NumberFilter()

    class Meta:
        model = Task
        fields = ['task_title', 'event_date', 'time_to_complete']


def search(request):
    """View for filtered task - not actually search"""
    task_list = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=task_list)
    return render(request, 'tasks/task_list.html', {'filter': task_filter})
