# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Phrase,
)


class PhraseCreateView(CreateView):

    model = Phrase


class PhraseDeleteView(DeleteView):

    model = Phrase


class PhraseDetailView(DetailView):

    model = Phrase


class PhraseUpdateView(UpdateView):

    model = Phrase


class PhraseListView(ListView):

    model = Phrase

