from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import List


class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title', 'description', 'listno']
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListCreate, self).form_valid(form)
