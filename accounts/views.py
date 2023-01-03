from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm

