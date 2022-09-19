#from curses.ascii import TAB
#from dataclasses import fields
from contextlib import redirect_stderr
from multiprocessing import AuthenticationError, context
from tkinter.tix import Tree
from turtle import title
from django.shortcuts import render ,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from base.models import Task
from django.contrib.auth.mixins import PermissionRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input']=search_input

        search_input_tags= self.request.GET.get('search-area-tags') or ''
        if search_input_tags:
            context['tasks'] = context['tasks'].filter(tags__startswith=search_input_tags)
        context['search_input_tags']=search_input_tags

        return context


