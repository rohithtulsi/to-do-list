from django.urls import path
from base.views.TaskDetail import TaskDetail
from base.views.TaskList import TaskList
from base.views.TaskCreate import TaskCreate
from base.views.TaskDelete import TaskDelete
from base.views.TaskUpdate import TaskUpdate
from base.views.ListCreate import ListCreate
from base.views.ListUpdate import ListUpdate
from base.views.ListDelete import ListDelete
from base.views.ListList import ListList


urlpatterns = [
    path('<int:listid>/tasks/', TaskList.as_view(), name='tasks'),
    path('<int:listid>/tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('tasks/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('create/', ListCreate.as_view(), name='list-create'),
    path('update/<int:pk>/', ListUpdate.as_view(), name='list-update'),
    path('delete/<int:pk>/', ListDelete.as_view(), name='list-delete'),
    path('', ListList.as_view(), name='lists'),
    # path('tasks/<int:pk>/', TaskDetail.as_view(), name='task'),
]
