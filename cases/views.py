from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'cases/base.html')

@login_required
def add_client(request):
    return render(request, 'cases/client.html')
