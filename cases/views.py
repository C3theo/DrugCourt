from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import (AssesmentForm, ClientForm, CourtDateForm, CourtFeeForm,
                    CourtPhaseForm, EmployerForm, ReferralForm, ReviewForm,
                    SanctionForm, TeamReviewForm, DrugScreenForm, CommunityServiceForm)


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

@login_required
def refer_client(request):

    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = ReferralForm()
    return render(request, 'cases/referral.html', {'form': form})

@login_required
def add_employer(request):

    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = EmployerForm()
    return render(request, 'cases/employer.html', {'form': form})

@login_required
def add_sanction(request):

    if request.method == 'POST':
        form = SanctionForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = SanctionForm()
    return render(request, 'cases/sanction.html', {'form': form})

@login_required
def add_court_phase(request):

    if request.method == 'POST':
        form = CourtPhaseForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = CourtPhaseForm()
    return render(request, 'cases/court_phase.html', {'form': form})

@login_required
def add_court_date(request):

    if request.method == 'POST':
        form = CourtDateForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = CourtDateForm()
    return render(request, 'cases/court_date.html', {'form': form})


@login_required
def add_court_fee(request):

    if request.method == 'POST':
        form = CourtFeeForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = CourtFeeForm()
    return render(request, 'cases/court_fee.html', {'form': form})

@login_required
def drug_screen(request):

    if request.method == 'POST':
        form = DrugScreenForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = DrugScreenForm()
    return render(request, 'cases/drug_screen.html', {'form': form})


@login_required
def comm_service(request):

    if request.method == 'POST':
        form = CommunityServiceForm(request.POST)
        if form.is_valid():

            #TODO: add client to database
            return HttpResponseRedirect('')
    else:
        form = CommunityServiceForm()
    return render(request, 'cases/comm_service.html', {'form': form})