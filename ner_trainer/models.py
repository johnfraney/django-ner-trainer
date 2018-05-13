# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from .validators import validate_all_caps


class ActivePhraseManager(models.Manager):
    def get_queryset(self):
        queryset = super(ActivePhraseManager, self).get_queryset()
        active_phrases = queryset.filter(skipped=False)
        return active_phrases


class TaggedPhraseManager(models.Manager):
    def get_queryset(self):
        queryset = super(TaggedPhraseManager, self).get_queryset()
        tagged_phrases = queryset.prefetch_related('entities').filter(
            skipped=False,
            entities__isnull=False).distinct()
        return tagged_phrases


class Phrase(TimeStampedModel):
    text = models.TextField(unique=True)
    skipped = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActivePhraseManager()
    tagged_objects = TaggedPhraseManager()

    def as_spacy_train_data(self):
        return (self.text, {'entities': [e.as_spacy_tuple() for e in self.entities.all()]})

    def __str__(self):
        return self.text


class Entity(TimeStampedModel):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100, validators=[validate_all_caps], primary_key=True)

    def get_absolute_url(self):
        return reverse('entity-recognizer:update', kwargs={'pk': self.label})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PhraseEntity(TimeStampedModel):
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE, related_name='entities')
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    start_index = models.SmallIntegerField()
    end_index = models.SmallIntegerField()

    def as_spacy_tuple(self):
        return (self.start_index, self.end_index, self.entity.label)
