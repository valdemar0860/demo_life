from django.urls import path
from .views import TaskListView

urlpatterns = [
    path('daily_tasks/', TaskListView.as_view(), name='task_list'),
]