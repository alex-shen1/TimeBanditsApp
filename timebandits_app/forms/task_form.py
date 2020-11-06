from django import forms
from ..models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = {
        "owner",
        "task_title",
        "task_description",
        "task_capacity",
        "event_date",
        "time_to_complete",
        "donation_amount",
        "event_address"}
        widgets = {
            'task_description': forms.Textarea(),
        }
