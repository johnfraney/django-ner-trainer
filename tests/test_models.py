#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-ner-trainer
------------

Tests for `django-ner-trainer` models module.
"""

from django.test import TestCase

from ner_trainer.models import (
    Entity,
    Phrase,
)


class TestEntity(TestCase):
    def test_str(self):
        entity = Entity(label='PROVINCE', name='Province')
        self.assertEqual(str(entity), 'Province')


class TestPhrase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestPhrase, cls).setUpClass()
        phrase = Phrase.objects.create(text='I like London and Berlin.')
        entity = Entity.objects.create(label='LOC', name='Location')
        phrase.entities.create(
            entity=entity,
            start_index=7,
            end_index=13,
        )
        phrase.entities.create(
            entity=entity,
            start_index=18,
            end_index=24,
        )
        cls.phrase = phrase

    def test_str(self):
        self.assertEqual(str(self.phrase), 'I like London and Berlin.')

    def test_active_phrase_manager(self):
        Phrase.objects.create(text="Skipped phrase", skipped=True)
        self.assertEqual(Phrase.objects.count(), 2)
        self.assertEqual(Phrase.active_objects.count(), 1)

    def test_tagged_phrase_manager(self):
        self.assertEqual(Phrase.tagged_objects.count(), 1)
        self.assertEqual(Phrase.tagged_objects.first(), self.phrase)

    def test_as_spacy_train_data(self):
        spacy_train_data = ('I like London and Berlin.', {
            'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]
        })
        self.assertEqual(self.phrase.as_spacy_train_data(), spacy_train_data)
