from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task, List


class TaskCompletion(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['complete']
    # success_url = reverse_lazy('lists')
    # template_name = 'base/task_list.html'

    def form_valid(self, form):
        form.instance.complete = True
        return super(TaskCompletion, self).form_valid(form)

    def get_success_url(self):
        return reverse('tasks', kwargs={'listid': self.object.listno.id})
