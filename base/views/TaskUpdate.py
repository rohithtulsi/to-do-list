from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task, List


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete', 'tags', 'listno']
    # success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super(TaskUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse('tasks', kwargs={'listid': self.object.listno.id})
