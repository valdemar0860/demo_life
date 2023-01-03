from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name="home/index.html"), name='index'),
    path('info/', TemplateView.as_view(template_name="home/info.html"), name='info'),
]
