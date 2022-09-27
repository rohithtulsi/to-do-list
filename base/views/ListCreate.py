from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import List
from base.models import AbstractModel


class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title', 'description',]
    success_url = reverse_lazy('lists')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ListCreate, self).form_valid(form)
