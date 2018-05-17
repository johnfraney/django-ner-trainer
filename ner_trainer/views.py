# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Entity,
    Phrase,
    PhraseEntity,
)
from .serializers import (
    EntitySerializer,
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
