"""
    Scribe Views
"""

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django_tables2.views import SingleTableView

from 
from .models import Note


class ClientNoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'intake/client_notes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'notes'
    paginate_by = 5

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_posted')



class NoteListView(LoginRequiredMixin, SingleTableView):
    model = Note
    table_class = NoteTable
    template_name = 'intake/clients_listing.html'
