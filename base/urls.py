from django.urls import path

from base.models import Task
from .views import TaskDetail, TaskList, CustomLoginView, RegisterPage
from base.views.TaskCreate import TaskCreate
from base.views.TaskDelete import TaskDelete
from base.views.TaskUpdate import TaskUpdate
from django.contrib.auth.views import LogoutView
from base.views.ListCreate import ListCreate
from base.views.ListUpdate import ListUpdate
from base.views.ListDelete import ListDelete
from base.views.ListList import ListList

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('list-create', ListCreate.as_view(), name='list-create'),
    path('list-update/<int:pk>/', ListUpdate.as_view(), name='list-update'),
     path('list-delete/<int:pk>/', ListDelete.as_view(), name='list-delete'),
    path('lists/', ListList.as_view(), name='lists'),
]
