from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task
from base.models import List
from base.forms import TaskForm


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    # success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.list_no = List.objects.get(id=self.kwargs['listid'])
        return super(TaskCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('tasks', kwargs={'listid': self.object.list_no.id})
