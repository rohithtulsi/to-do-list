from django.urls import path
from .views import TaskDetail, TaskList
from base.views.TaskCreate import TaskCreate
from base.views.TaskDelete import TaskDelete
from base.views.TaskUpdate import TaskUpdate
from base.views.ListCreate import ListCreate
from base.views.ListUpdate import ListUpdate
from base.views.ListDelete import ListDelete
from base.views.ListList import ListList
from base.views.CustomLoginView import CustomLoginView
from base.views.RegisterPage import RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    # path('<int:pk>/tasks/', TaskList.as_view(), name='tasks'),
    # path('<int:pk>/task/<int:pk>/', TaskDetail.as_view(), name='task'),
    # path('<int:pk>/task/create', TaskCreate.as_view(), name='task-create'),
    # path('<int:pk>/task/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    # path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('list/create', ListCreate.as_view(), name='list-create'),
    path('list/update/<int:pk>', ListUpdate.as_view(), name='list-update'),
    path('list/delete/<int:pk>', ListDelete.as_view(), name='list-delete'),
    path('', ListList.as_view(), name='lists'),
    # path('lists/list/', TaskList.as_view(), name='tasks'),
]
