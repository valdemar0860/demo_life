from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'home/index.html'


class InfoPageView(TemplateView):
    template_name = 'home/info.html'
