from django.core.management.base import BaseCommand

from ner_trainer.conf import settings
from ner_trainer.models import Entity, Phrase
from ner_trainer.spacy_utils import train_ner


class Command(BaseCommand):
    help = 'Trains your custom spaCy model'

    def handle(self, *args, **options):
        model_directory = settings.NER_TRAINER_MODEL_DIRECTORY
        model_name = settings.NER_TRAINER_MODEL_NAME
        train_iterations = settings.NER_TRAINER_MODEL_TRAIN_ITERATIONS
        entity_labels = Entity.objects.values_list('label', flat=True)
        phrases = Phrase.tagged_objects.all()
        train_data = [p.as_spacy_train_data() for p in phrases]
        self.stdout.write(self.style.NOTICE(
            'Training NER model with {} iterations'.format(train_iterations)
        ))
        train_ner(entity_labels=entity_labels,
                  train_data=train_data,
                  model_name=model_name,
                  model_directory=model_directory,
                  n_iter=train_iterations)
        self.stdout.write(self.style.SUCCESS('Model updated'))
