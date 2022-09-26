from django.urls import path
from .views import TaskDetail, TaskList
from base.views.TaskCreate import TaskCreate
from base.views.TaskDelete import TaskDelete
from base.views.TaskUpdate import TaskUpdate
from base.views.ListCreate import ListCreate
from base.views.ListUpdate import ListUpdate
from base.views.ListDelete import ListDelete
from base.views.ListList import ListList

urlpatterns = [
    path('<int:pk>/tasks/', TaskList.as_view(), name='tasks'),
    path('<int:pk>/task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('<int:pk>/task/create', TaskCreate.as_view(), name='task-create'),
    path('<int:pk>/task/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('list-create', ListCreate.as_view(), name='list-create'),
    path('list-update/<int:pk>/', ListUpdate.as_view(), name='list-update'),
    path('list-delete/<int:pk>/', ListDelete.as_view(), name='list-delete'),
    path('lists/', ListList.as_view(), name='lists'),
    path('lists/list/', TaskList.as_view(), name='tasks'),
]
