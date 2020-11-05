"""Views related to tasks."""""
# pylint: disable=too-many-ancestors,invalid-name
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import stripe
import json

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
                return render(request, 'tasks/checkout.html', {'form': form})
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

@csrf_exempt
def createpayment(request):
    """Pays the donation amount of a task"""
    stripe.api_key = 'sk_test_51Hi2a6DLHK87XPh2eZS2T6z5TzsOQ9nsWUWfxyKUtYXNGPM5HWQYL70bK0S7y9kL13i2VGwkvcwjmqGdiu56Znib00S9IYDOZl'
    if request.method == 'POST':
        form = TaskForm(request.POST)
        charge = stripe.PaymentIntent.create(
            amount=500,
            currency='usd',
            metadata={'integration_check': 'accept_a_payment'},
            )
        try:
            return JsonResponse({'publishableKey': 'your test publishable key', 'clientSecret': charge.client_secret})
        except Exception as e:
            return JsonResponse({'error':str(e)},status= 403)

def paymentcomplete(request):
	#if request.method=="POST":
		#data = json.loads(request.POST.get("payload"))
    return HttpResponseRedirect('/tasks')

def get_context_data(self, **kwargs):
    """Sets the key for the payment"""
    context = super().get_context_data(**kwargs)
    context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    return context

class TaskDetailsView(generic.DetailView):
    """Displays details for a particular Task."""
    template_name = 'tasks/task_details.html'
    model = Task
