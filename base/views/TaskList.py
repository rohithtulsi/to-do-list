from asyncio import tasks
from urllib import request
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task
from base.models import List
from base.views.TaskUpdate import TaskUpdate
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from base.models import Task, List
from django.shortcuts import redirect
from base.filters import OrderFilter

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    fields = ['complete']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(created_by=self.request.user, listno=self.kwargs['listid'])
        context['count'] = context['tasks'].filter(complete=False).count()
        context['list'] = List.objects.get(id=self.kwargs['listid'])
        context['listname'] = List.objects.get(id=self.kwargs['listid'])
                
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input

        search_input_Priority = self.request.GET.get('search-area-Priority') 
        
        if search_input_Priority:
            context['tasks'] = context['tasks'].filter(Priority=search_input_Priority)
        context['search_input_Priority'] = search_input_Priority
        
        return context
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        form.instance.complete = self.request.GET.get('task-status')
        form.instance.save()
        return redirect('tasks',listid=self.kwargs['listid'])
    
    def get_success_url(self):
        return reverse('tasks', kwargs={'listid': self.object.listno.id})

