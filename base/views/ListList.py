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

from base.models import List
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListList(LoginRequiredMixin,ListView):
    model = List
    context_object_name = 'lists'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user=self.request.user)

        
        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['lists'] = context['lists'].filter(title__startswith=search_input)
        context['search_input']=search_input

        return context
