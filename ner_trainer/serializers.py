# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Entity, Phrase, PhraseEntity


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = ('name', 'label')


class PhraseEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhraseEntity
        fields = ('id', 'phrase', 'entity', 'start_index', 'end_index')


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = ('id', 'text', 'skipped', 'entities')
        depth = 1


class ModelTestSerializer(serializers.Serializer):
    text = serializers.CharField()
