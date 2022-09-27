from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import List


class ListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['title', 'description']
    success_url = reverse_lazy('lists')
