from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2.views import SingleTableView
from viewflow.flow.views import FlowMixin

from intake.forms import (ClientForm, DecisionForm, NoteForm, NoteFormSet,
                          ReferralForm, ClientFormset)
from intake.models import Client, Decision, Note, Referral

from .tables import ClientTable, NoteTable


class ReferralCreateView(LoginRequiredMixin, CreateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'core/form_base.html'


class ReferralDetailView(LoginRequiredMixin, UpdateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'core/form_base.html'


class DecisionCreateView(CreateView):
    model = Decision
    form_class = DecisionForm
    template_name = 'core/form_base.html'

    def form_valid(self, form):
        # self.object = form.save(commit=False)

        # self.object.user = self.request.user
        # self.object.process = self.activation.process
        # self.object.save()

        # self.activation.done()
        # self.success('Task {task} has been completed.')

        return HttpResponseRedirect(self.get_success_url())


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name_suffix = '_update_form'


class ClientDetailView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name_suffix = '_update_form'


class ClientListView(LoginRequiredMixin, SingleTableView):
    model = Client
    table_class = ClientTable
    template_name = 'intake/clients_listing.html'
    context_object_name = 'clients'


class ClientNoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'intake/client_notes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    paginate_by = 5

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_posted')


class ClientNoteCreateView(CreateView):
    model = Client
    template_name = 'intake/note_create.html'
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
            self.object = form.save()
            if client_notes.is_valid():
                client_notes.instance = self.object
                client_notes.save()

        return super(ClientNoteCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('intake:note-add')


class NoteListView(LoginRequiredMixin, SingleTableView):
    model = Note
    table_class = NoteTable
    template_name = 'intake/clients_listing.html'


class IntakeFormView(LoginRequiredMixin, SingleObjectMixin, TemplateView):
    template_name = 'intake/intake_form.html'
    model = Client

    # def __init__(self, **kwargs):

    #     super(IntakeFormView, TemplateView).__init__(**kwargs)
    #     self.object = Client.objects.filter(pk=1)

    # def get_form_class(self):

    # def get_form_kwargs(self):

    # def get_context_data(self, **kwargs):
    #     context = {'client_form': ClientForm(prefix='client'),
    #               'note_form': NoteForm(prefix='note'),
    #               'referral_form': ReferralForm(prefix='referral'),
    #               'decision_form': DecisionForm(prefix='decision')}
    #     return super().get_context_data(**context)

    def get(self, request, *args, **kwargs):
        """
        """
        # BaseUpdateView
        # import pdb
        # pdb.set_trace()
        # if self.request.path == '/intake/new/':
        return self.render_to_response({'client_form': ClientForm(prefix='client'),
                                        'note_form': NoteForm(prefix='note'),
                                        'referral_form': ReferralForm(prefix='referral'),
                                        'decision_form': DecisionForm(prefix='decision')})
        # else:
        #     self.object = self.get_object()
        #     # import pdb
        #     # pdb.set_trace()
        #     # test = self.get_context_data(**kwargs)
        #     return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        """
            Save form instance depending on form prefix.

            Return Response object with forms in context.
        """

        client_form = _get_form_submit(
            request, ClientForm, prefix='client')
        note_form = _get_form_submit(request, NoteForm, prefix='note')
        referral_form = _get_form_submit(
            request, ReferralForm, prefix='referral')
        decision_form = _get_form_submit(
            request, DecisionForm, prefix='decision')

        # import pdb
        # pdb.set_trace()

        if client_form.is_bound and client_form.is_valid():
            instance = client_form.save()
            messages.success(
                request, f'Client {instance.client_id} saved successfully.')
            # return reverse()
            # return HttpResponseRedirect(instance.get_success_url())

        elif note_form.is_bound and note_form.is_valid():
            instance = note_form.save()
            messages.success(request, f'Referral saved successfully.')
            # TODO: Add ForeignKeyField client

        elif referral_form.is_bound and referral_form.is_valid():
            instance = referral_form.save()
            messages.success(
                request, f'Note created at {instance.created_date}.')
            # return HttpResponseRedirect(instance.client.get_success_url())
        elif decision_form.is_bound and decision_form.is_valid():
            instance = decision_form.save()
            messages.success(
                request, f'Referral Decision saved.')

        return self.render_to_response({'client_form': client_form, 'note_form': note_form,
                                        'referral_form': referral_form, })
# 'decision_form': decision_form


def _get_form_submit(request, formcls, prefix=None):
    """
        Return bound form object if prefix is in POST request.

        Args:
            request:
            formcls:
            prefix
    """

    data = request.POST if prefix in request.POST.keys() else None

    return formcls(data, prefix=prefix)
