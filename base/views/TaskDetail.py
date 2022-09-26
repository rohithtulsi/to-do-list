from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
