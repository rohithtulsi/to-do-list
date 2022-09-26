from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import List


class ListList(LoginRequiredMixin, ListView):
    model = List
    context_object_name = 'lists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user=self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['lists'] = context['lists'].filter(title__startswith=search_input)
        context['search_input'] = search_input

        return context
