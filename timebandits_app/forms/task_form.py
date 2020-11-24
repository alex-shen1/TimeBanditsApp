from django import forms
from ..models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            # "owner", # leave out owner bc we set that in the view
            "task_title",
            "task_description",
            "task_capacity",
            "event_date",
            "event_time",
            "time_to_complete",
            "donation_amount",
            "event_address"]
        widgets = {
            'task_description': forms.Textarea(),
        }
