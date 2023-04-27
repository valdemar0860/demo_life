from django.urls import path
from .views import MainPageView, InfoPageView

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('info/', InfoPageView.as_view(), name='info'),
]
