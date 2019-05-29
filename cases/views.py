from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from .forms import ClientForm, ReviewForm, TeamReviewForm, AssesmentForm

@login_required
def home(request):
    return render(request, 'cases/base.html')

@login_required
def add_client(request):

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            #TODO: add client to database
            return HttpResponseRedirect('review/')
    else:
        form = ClientForm()
    return render(request, 'cases/add_client.html', {'form': form})

@login_required
def review_client(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = ReviewForm()
    return render(request, 'cases/review.html', {'form': form})

@login_required
def assess_client(request):

    if request.method == 'POST':
        form = AssesmentForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = AssesmentForm()
    return render(request, 'cases/assessment.html', {'form': form})