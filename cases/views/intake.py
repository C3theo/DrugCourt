from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from ..forms import ClientForm, NoteForm, ReferralForm
from ..models import Client, Note, Referral


class IntakeFormView(LoginRequiredMixin, TemplateView):
    template_name = 'cases/intake_form.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()

    #     context.update({'client_form': ClientForm(prefix='client'),
    #                     'note_form': NoteForm(prefix='note'),
    #                     'referral_form': ReferralForm(prefix='referral'), })
    #     return context

    def get(self, request, *args, **kwargs):
        """
        """
        return self.render_to_response({'client_form': ClientForm(prefix='client'),
                                        'note_form': NoteForm(prefix='note'),
                                        'referral_form': ReferralForm(prefix='referral'), })

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


        if client_form.is_bound and client_form.is_valid():
            instance = client_form.save()
            messages.success(
                request, f'Client {instance.client_id} saved successfully.')

        elif note_form.is_bound and note_form.is_valid():
            instance = note_form.save()
            messages.success(request, f'Referral saved successfully.')
            # TODO: Add ForeignKeyField client to fstring

        elif referral_form.is_bound and referral_form.is_valid():
            instance = referral_form.save()
            messages.success(
                request, f'Note created at {instance.created_date}.')

        return self.render_to_response({'client_form': client_form, 'note_form': note_form,
                                        'referral_form': referral_form})


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
