from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task
from base.models import List


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    fields = ['complete']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(created_by=self.request.user, list_no=self.kwargs['listid'])
        context['count'] = context['tasks'].filter(complete=False).count()
        context['count2'] = context['tasks'].filter(complete=True).count()
        context['total'] = context['tasks'].count()
        context['list'] = List.objects.get(id=self.kwargs['listid'])
        context['listname'] = List.objects.get(id=self.kwargs['listid'])

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__contains=search_input)
        context['search_input'] = search_input

        search_input_incomplete = self.request.GET.get('incomplete') or ''
        if search_input_incomplete:
            context['tasks'] = context['tasks'].filter(complete=False)
            if self.request.GET.get('incomplete'):
                Complete_b = bool(self.request.GET.get('incomplete'))
                context.update({'InComplete_b': True, })

        search_input_complete = self.request.GET.get('complete') or ''
        if search_input_complete:
            context['tasks'] = context['tasks'].filter(complete=True)
            if self.request.GET.get('complete'):
                Complete_b = bool(self.request.GET.get('complete'))
                context.update({'Complete_b': True, })

        search_input_Priority = self.request.GET.get('check') or self.request.GET.get('check1') or self.request.GET.get('check2') or self.request.GET.get('check3')
        if search_input_Priority:
            context['tasks'] = context['tasks'].filter(priority=self.request.GET.get('check1')) | context['tasks'].filter(priority=self.request.GET.get('check2')) | context['tasks'].filter(priority=self.request.GET.get('check3'))
            if self.request.GET.get('check1'):
                High_b = bool(self.request.GET.get('Check1'))
                context.update({'High_b': True, })
            if self.request.GET.get('check2'):
                Normal_b = bool(self.request.GET.get('Check2'))
                context.update({'Normal_b': True, })
            if self.request.GET.get('check3'):
                Low_b = bool(self.request.GET.get('Check3'))
                context.update({'Low_b': True, })
        context['search_input_Priority'] = search_input_Priority

        return context
