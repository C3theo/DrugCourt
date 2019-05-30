from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import ClientTabForm, CourtTabForm


@login_required
def home(request):
    return render(request, 'cases/home.html', context={'current':'(current)'})

@login_required()
def client_tabs(request):
    form = ClientTabForm()
    return render(request, 'cases/client_tabs.html', {'form': form})

@login_required()
def court_tabs(request):
    form = CourtTabForm()
    return render(request, 'cases/court_tabs.html', {'form': form})