from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django_tables2.views import SingleTableView, MultiTableMixin

from scribe.forms import NoteForm, NoteFormSet
from scribe.models import Note
from scribe.tables import NoteTable

from .filters import ClientFilter, ReferralFilter
from ..forms import (ClientForm, ClientFormset, ClientReferralMultiForm,
                     CriminalBackgroundForm, DecisionForm,
                     ReferralDecisionMultiForm, ReferralForm, ReferralQueryForm)
from ..models import Client, CriminalBackground, Decision, Referral
from .tables import ClientTable, ClientCourtTable


def client_list(request):

    client_list = Client.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(client_list, 25)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    return render(request, 'intake/client_list.html', {'clients': clients})

def paginate_clients(request, data, by=25):

    client_list = Client.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(client_list)

    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)

    data['html_client_list'] = render_to_string(
        'intake/includes/partial_client_list.html', {'clients': clients})

    return data

def save_client_form(request, template_name, forms=None, context=None):
    """
        Helper function for adding form to context.
    """
    data = dict()

    if request.method == 'POST':
        for form in forms:
            if form.is_valid():

                data['form_is_valid'] = True
                data = paginate_clients(request, data)
            # save Note Form
            # try:
            #     # ???
            #     client = context['client']
            #     note = form.save(commit=False)
            #     note.author = request.user
            #     note.save()
                
            # except (KeyError, TypeError):
            #     form.save()

        else:
            data['form_is_valid'] = False
    
    # if context:
    #     context['form'] = form
    # else:
    #     context = {"form": form}


    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def client_create(request):
    """
        Handle GET/POST requests and instantiate forms.
    """

    if request.method == 'POST':
        form = ClientReferralMultiForm(request.POST)
    else:
        form = ClientReferralMultiForm()
    return save_client_form(request, form, 'intake/includes/partial_client_create.html')


def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client_form = ClientForm(request.POST, instance=client)
        referral_form = ReferralForm(request.POST, instance=client.referral)
        # form = ClientReferralMultiForm(request.POST, instance={
        #     'client': client,
        #     'referral': client.referral
        # })
    else: # GET Request
        
        client_form = ClientForm(instance=client)
        referral_form = ReferralForm(instance=client.referral)

        # form = ClientReferralMultiForm(instance={
        #     'client': client,
        #     'referral': client.referral
        # })

    return save_client_form(request, form, 'intake/includes/partial_client_update.html')


def client_evaluate(request, pk):

    referral = get_object_or_404(Referral, pk=pk)
    decisions = referral.decisions
    if request.method == 'POST':
        form = ReferralDecisionMultiForm(request.POST, instance={
            'referral': referral,
            'pre_decision': decisions[0],
            'da_decision': decisions[1],
            'dc_decision': decisions[2],
        })
    else:
        form = ReferralDecisionMultiForm(instance={
            'referral': referral,
            'pre_decision': decisions[0],
            'da_decision': decisions[1],
            'dc_decision': decisions[2],
        })

    return save_client_form(request, form, 'intake/includes/partial_client_evaluate.html')

def client_note(request, pk):

    client = get_object_or_404(Client, pk=pk)
    context = {'client': client}
    if request.method == 'POST':
        form = NoteForm(request.POST, initial={'note_type': 'General'})
    else:
        form = NoteForm(initial={'note_type': 'General'})

    return save_client_form(request, form, 'intake/includes/partial_client_note.html', context=context)



class IntakeFilterView(LoginRequiredMixin, SingleTableView):
    """
        Intake Start Page
    """

    template_name = 'intake/0_client_referral_filter.html'
    model = Client
    table_class = ClientTable


class ReferralDecisionUpdateView(LoginRequiredMixin, UpdateView):
    """
        Intake Client/Referral UpdateView
    """
    model = Referral
    form_class = ReferralDecisionMultiForm
    template_name = 'intake/2_referral_decision.html'
    success_url = reverse_lazy('intake:start')

    def get_form_kwargs(self):
        """
            Add Referral and 3 Associated decision objects to form.
        """

        kwargs = super(ReferralDecisionUpdateView, self).get_form_kwargs()

        # TODO: change Decision.ROLE to be able to accesss in form
        # This will make it so you can add decisions dynamically
        # decisions = {f'{each.made_by}_decision': each for each in self.object.decisions}
        # decisions = {f'decision_{i}': each for i, each in enumerate(self.object.decisions)}
        # instance={'referral': self.object}
        # instance.update(decisions)
        # kwargs.update(instance=instance)

        decisions = self.object.decisions
        kwargs.update(instance={
            'referral': self.object,
            'pre_decision': decisions[0],
            'da_decision': decisions[1],
            'dc_decision': decisions[2],
        })

        return kwargs


class ClientReferralUpdateView(LoginRequiredMixin, UpdateView):
    """
    """

    model = Referral
    form_class = ClientReferralMultiForm
    template_name = 'intake/1_client_referral.html'

    def get_context_data(self, **kwargs):
        """
            Initialize NoteForm with client and pass to context
        """

        note_form = NoteForm(prefix='note')
        context = {'note_form': note_form}
        return super().get_context_data(**context)

    def post(self, request, *args, **kwargs):
        """
            Submit NoteForm separately from Referral/ClientForm.
        """

        referral = self.get_object()
        self.success_url = referral.get_absolute_url()  # ???
        note_form = _get_form_submit(
            request, NoteForm, prefix='note')
        if note_form.is_bound and note_form.is_valid():
            note_form.instance.author = self.request.user
            note_form.instance.client = referral.client
            instance = note_form.save()
            messages.success(
                request, f'Note for {instance.client.full_name} ID: {instance.client.client_id}  saved successfully!')
            return self.form_valid(note_form)

        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
            Return the keyword arguments for instantiating client and referral forms.
        """

        kwargs = super(ClientReferralUpdateView, self).get_form_kwargs()
        kwargs.update(instance={
            'client': self.object.client,
            'referral': self.object
        })

        return kwargs


class ClientReferralCreateView(LoginRequiredMixin, CreateView):
    """
        Intake Client/Referral CreationView
    """

    model = Referral
    form_class = ClientReferralMultiForm
    template_name = 'intake/1_client_referral.html'
    success_url = reverse_lazy('intake:start')


class ClientNoteCreateView(LoginRequiredMixin, CreateView):
    """
        View using Note Formsets
    """
    model = Client
    template_name = 'intake/note.html'
    form_class = ClientFormset
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(ClientNoteCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['client_notes'] = NoteFormSet(
                self.request.POST, prefix='notes')
        else:
            data['client_notes'] = NoteFormSet(prefix='notes')
        return data

    def form_valid(self, form):

        context = self.get_context_data()
        client_notes = context['client_notes']
        with transaction.atomic():
            form.instance.author = self.request.username
            import pdb
            pdb.set_trace()
            self.object = form.save()
            if client_notes.is_valid():
                client_notes.instance = self.object
                client_notes.save()

        return super(ClientNoteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('intake:note-add')


class CriminalBackgroundCreateView(LoginRequiredMixin, CreateView):
    model = CriminalBackground
    form_class = CriminalBackgroundForm
    template_name = 'intake/criminal_background.html'


class DecisionCreateView(LoginRequiredMixin, CreateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'intake/decision.html'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'intake/client.html'


class ClientListView(LoginRequiredMixin, SingleTableView):
    model = Client
    table_class = ClientTable
    template_name = 'intake/client_filter.html'
    context_object_name = 'clients'


# class IntakeFormUpdateView(LoginRequiredMixin, CreateView):
#     """
#         Multi object UpdateView
#     """
#     model = Referral
#     template_name = 'intake/0_client_referral_filter.html'

    # def __init__(self, **kwargs):

    #     super(IntakeFormView, TemplateView).__init__(**kwargs)
    #     self.object = Client.objects.filter(pk=1)

    # def get_context_data(self, **kwargs):
    #     context = {'client_form': ClientForm(prefix='client'),
    #               'note_form': NoteForm(prefix='note'),
    #               'referral_form': ReferralForm(prefix='referral'),
    #               'decision_form': DecisionForm(prefix='decision')}
    #     return super().get_context_data(**context)

    # def get(self, request, *args, **kwargs):
    #     """
    #     """

    #     return self.render_to_response({'client_form': ClientForm(prefix='client'),
    #                                     'note_form': NoteForm(prefix='note'),
    #                                     'referral_form': ReferralForm(prefix='referral'),
    #                                     'decision_form': DecisionForm(prefix='decision')})
    #     # else:
    #     #     self.object = self.get_object()
    #     #     # import pdb
    #     #     # pdb.set_trace()
    #     #     # test = self.get_context_data(**kwargs)
    #     #     return self.render_to_response(self.get_context_data(**kwargs))

    # def post(self, request, *args, **kwargs):
    #     """
    #         Save form instance depending on form prefix.

    #         Return Response object with forms in context.
    #     """

    #     client_form = _get_form_submit(
    #         request, ClientForm, prefix='client')
    #     note_form = _get_form_submit(request, NoteForm, prefix='note')
    #     referral_form = _get_form_submit(
    #         request, ReferralForm, prefix='referral')
    #     decision_form = _get_form_submit(
    #         request, DecisionForm, prefix='decision')

    #     if client_form.is_bound and client_form.is_valid():
    #         instance = client_form.save()
    #         messages.success(
    #             request, f'Client {instance.client_id} saved successfully.')
    #         # return reverse()
    #         # return HttpResponseRedirect(instance.get_success_url())

    #     elif note_form.is_bound and note_form.is_valid():
    #         instance = note_form.save()
    #         messages.success(request, f'Referral saved successfully.')
    #         # TODO: Add ForeignKeyField client

    #     elif referral_form.is_bound and referral_form.is_valid():
    #         instance = referral_form.save()
    #         messages.success(
    #             request, f'Note created at {instance.created_date}.')
    #         # return HttpResponseRedirect(instance.client.get_success_url())
    #     elif decision_form.is_bound and decision_form.is_valid():
    #         instance = decision_form.save()
    #         messages.success(
    #             request, f'Referral Decision saved.')

    #     return self.render_to_response({'client_form': client_form, 'note_form': note_form,
    #                                     'referral_form': referral_form, 'decision_form': decision_form})


def _get_form_submit(request, formcls, prefix=None):
    """
        Return bound form object if prefix is in POST request.

        Args:
            request:
            formcls:
            prefix
    """
    data = request.POST if prefix in request.POST.keys() else None
    # data = request.POST

    return formcls(data, prefix=prefix)
