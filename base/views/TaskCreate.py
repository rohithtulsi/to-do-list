from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task
from base.models import List


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete', 'tags']
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.listno = List.objects.get(id=self.kwargs['listid'])
        return super(TaskCreate, self).form_valid(form)

    