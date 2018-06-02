import shutil
from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase

from ner_trainer.models import (
    Entity,
    Phrase,
)


class EntityTests(APITestCase):
    def test_entity_list(self):
        """
        Ensure we can list Entity objects.
        """
        for i in range(5):
            name = 'Entity {}'.format(i)
            label = 'ENTITY_{}'.format(i)
            Entity.objects.create(name=name, label=label)
        response = self.client.get('/entities/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_entity_detail(self):
        """
        Ensure we can detail an Entity object.
        """
        Entity.objects.create(name='Banana', label='BANANA')
        response = self.client.get('/entities/BANANA/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Banana')
        self.assertEqual(response.data['label'], 'BANANA')


class PhraseTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(PhraseTests, cls).setUpClass()

    def test_phrase_list(self):
        """
        Ensure we can list Phrase objects.
        """
        Phrase.objects.create(text='Phrase 1')
        response = self.client.get('/phrases/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['text'], 'Phrase 1')

    def test_active_phrase_list(self):
        """
        Ensure we can list active Phrase objects.
        """
        phrases = []
        for i in range(10):
            text = 'Phrase {}'.format(i)
            phrases.append(Phrase(text=text))
        Phrase.objects.bulk_create(phrases)
        response = self.client.get('/phrases/active/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
        self.assertEqual(response.data[0]['text'], 'Phrase 0')
        self.assertEqual(response.data[-1]['text'], 'Phrase 9')

    def test_tagged_phrase_list(self):
        """
        Ensure we can list tagged Phrase objects.
        """
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
        response = self.client.get('/phrases/tagged/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class NERModelTestViewTests(APITestCase):
    def test_get(self):
        response = self.client.get('/test-ner/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_with_text_without_model(self):
        data = {'text': 'This is a sentence.'}
        response = self.client.post('/test-ner/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('Could not find NER model' in response.data)

    def test_post_without_text(self):
        data = {}
        response = self.client.post('/test-ner/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('Missing required field' in response.data)

    def test_post_with_model(self):
        call_command('train_ner_model')
        text = 'This is a sentence.'
        data = {'text': text}
        response = self.client.post('/test-ner/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_response_data = {
            'text': 'This is a sentence.',
            'entities': []
        }
        self.assertEqual(response.data, expected_response_data)
        shutil.rmtree('spacy_model', ignore_errors=True)
