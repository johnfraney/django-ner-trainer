# -*- coding: utf-8 -*-
import spacy
from django.http import HttpResponse
from pathlib import Path
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .conf import settings

from .models import (
    Entity,
    Phrase,
    PhraseEntity,
)
from .serializers import (
    EntitySerializer,
    ModelTestSerializer,
    PhraseSerializer,
    PhraseEntitySerializer,
)


class ListActionMixin:
    def list_action(self, queryset):
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class PhraseViewSet(viewsets.ModelViewSet, ListActionMixin):
    """
    get:
    Return a list of all phrases.

    active:
    Return a list of phrases that have not been skipped.

    tagged:
    Return a list of tagged phrases.
    """
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

    @action(detail=False)
    def active(self, request):
        active_phrases = Phrase.active_objects.all()
        return self.list_action(active_phrases)

    @action(detail=False)
    def tagged(self, request):
        tagged_phrases = Phrase.tagged_objects.all()
        return self.list_action(tagged_phrases)


class PhraseEntityViewSet(viewsets.ModelViewSet):
    queryset = PhraseEntity.objects.all()
    serializer_class = PhraseEntitySerializer


class NERModelTestView(APIView):
    """View to test a trained NER model"""
    serializer_class = ModelTestSerializer

    def get_view_name(self):
        return 'NER Model Test'

    def get(self, request, format=None):
        return Response(['Post a text field to test the NER model.'])

    def post(self, request):
        text = request.data.get('text', None)
        if not text:
            return Response("Missing required field: text")
        model_path = Path(settings.NER_TRAINER_MODEL_DIRECTORY)
        if not model_path.exists():
            return Response(
                "Could not find NER model at {}. Was it trained?".format(
                    model_path.resolve()
                )
            )
        nlp = spacy.load(model_path)
        doc = nlp(text)
        entities = [{
            'text': ent.text,
            'label': ent.label_,
            'start_index': ent.start_char,
            'end_index': ent.end_char
        } for ent in doc.ents]

        return Response({
            'text': str(doc),
            'entities': entities,
        })
