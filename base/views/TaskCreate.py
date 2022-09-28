from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task, List


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete', 'tags', 'listno']
    success_url = reverse_lazy('lists')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TaskCreate, self).form_valid(form)
