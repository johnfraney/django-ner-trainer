# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Entity, Phrase, PhraseEntity


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity
        fields = ('url', 'name', 'label')


class PhraseEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhraseEntity
        fields = ('url', 'id', 'phrase', 'entity', 'start_index', 'end_index')


class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phrase
        fields = ('url', 'id', 'text', 'skipped')
