from django import forms
from django.forms import ModelForm

from base.models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'priority','due_date']
        widgets = {
            'due_date': DateInput(),
        }

class TaskUForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'priority', 'list_no','due_date']
        widgets = {
            'due_date': DateInput(),
        }