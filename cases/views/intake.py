from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView

from ..models import Referral, Client, Note
from ..forms import ClientForm, NoteForm, ReferralForm


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in next(iter(request.POST.keys())) else None
    return formcls(data, prefix=prefix)


class RequestUserMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context


class IntakeView(LoginRequiredMixin, TemplateView):
    template_name = 'cases/intake_form.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'client_form': ClientForm(prefix='client'),
                                        'note_form': NoteForm(prefix='note'),
                                        'referral_form': ReferralForm(prefix='referral'), })

    def post(self, request, *args, **kwargs):

        client_form = _get_form(request, ClientForm, 'client')
        note_form = _get_form(request, NoteForm, 'note')
        referral_form = _get_form(request, ReferralForm, 'note')

        if client_form.is_bound and client_form.is_valid():
            pass
            # Process aform and render response
        elif note_form.is_bound and note_form.is_valid():
            note_form.data['author'] = request.user
            # Process bform and render response
        elif referral_form.is_bound and referral_form.is_valid():
            pass
            # Process bform and render response
        return self.render_to_response({'client_form': client_form, 'note_form': note_form,
                                        'referral_form': referral_form})

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

# class ReferralCreateView(LoginRequiredMixin, CreateView):
#     model = Referral
#     form_class = ClientForm
#     template_name = 'cases/intake_form.html'
