from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from base.models import Task
from django.contrib.auth.mixins import PermissionRequiredMixin


class TaskDelete(PermissionRequiredMixin, DeleteView):
    model = Task
    permission_required = 'delete_task'
    context_object_name = 'task'
    success_url = reverse_lazy('lists')
