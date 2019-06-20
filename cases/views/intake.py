from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView

from ..models import Referral, Client, Note
from ..forms import ClientForm, NoteForm, ReferralForm


class IntakeView(LoginRequiredMixin, TemplateView):
    template_name = 'cases/intake_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context.update({'client_form': ClientForm(prefix='client'),
                        'note_form': NoteForm(prefix='note'),
                        'referral_form': ReferralForm(prefix='referral'), })
        return context

# Note: TemplateView has no post method
    def post(self, request, *args, **kwargs):
        """
            Save form instance depending on the form prefix. 
        """

        client_form = _get_form(request, ClientForm, 'client')
        note_form = _get_form(request, NoteForm, 'note')
        referral_form = _get_form(request, ReferralForm, 'note')

        if client_form.is_bound and client_form.is_valid():
            instance = client_form.save()
            # TODO: add messages
        elif note_form.is_bound and note_form.is_valid():
            instance = note_form.save()
        elif referral_form.is_bound and referral_form.is_valid():
            instance = referral_form.save()

        return self.render_to_response({'client_form': client_form, 'note_form': note_form,
                                        'referral_form': referral_form})

def _get_form(request, formcls, prefix):
    """
        Return bound form object if prefix is POST data.
    """
    data = request.POST if prefix in next(
        iter(request.POST.keys())) else None
    return formcls(data, prefix=prefix)
