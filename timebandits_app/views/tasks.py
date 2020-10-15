"""Views related to tasks."""""
# pylint: disable=too-many-ancestors

from django.views import generic
from ..models import Task


# don't really know what kind of view from generic should be used
class TasksView(generic.ListView):
    """Lists all available Tasks."""
    # shouldn't the map be part of this view?
    template_name = 'tasks/tasks.html'
    model = Task


class CreateTasksView(generic.TemplateView):
    """Form where user can create a Task."""
    template_name = 'tasks/create_task.html'
    model = Task


class TaskDetailsView(generic.DetailView):
    """Displays details for a particular Task."""
    template_name = 'tasks/task_details.html'
    model = Task
