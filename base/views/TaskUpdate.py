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

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    
    success_url = reverse_lazy('tasks')