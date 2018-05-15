# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


app_name = 'ner_trainer'
urlpatterns = [
    url(
        regex="^Phrase/~create/$",
        view=views.PhraseCreateView.as_view(),
        name='Phrase_create',
    ),
    url(
        regex="^Phrase/(?P<pk>\d+)/~delete/$",
        view=views.PhraseDeleteView.as_view(),
        name='Phrase_delete',
    ),
    url(
        regex="^Phrase/(?P<pk>\d+)/$",
        view=views.PhraseDetailView.as_view(),
        name='Phrase_detail',
    ),
    url(
        regex="^Phrase/(?P<pk>\d+)/~update/$",
        view=views.PhraseUpdateView.as_view(),
        name='Phrase_update',
    ),
    url(
        regex="^Phrase/$",
        view=views.PhraseListView.as_view(),
        name='Phrase_list',
    ),
]
