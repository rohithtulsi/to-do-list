from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import List


class ListDelete(LoginRequiredMixin, DeleteView):
    model = List
    context_object_name = 'list'
    success_url = reverse_lazy('lists')
