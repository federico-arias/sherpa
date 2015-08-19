from django import forms
from .models import Task

class TaskForm(forms.Form):
    class Meta:
        model=Task
        fields=('tasktype', 'due_date', 'attached_source', 'project')
