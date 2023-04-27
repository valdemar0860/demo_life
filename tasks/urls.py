from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TaskListViewREST, TaskListView

router = SimpleRouter()

router.register('api/tasks', TaskListViewREST)

urlpatterns = [
    path('daily_tasks/', TaskListView.as_view(), name='daily_tasks'),
]
urlpatterns += router.urls
