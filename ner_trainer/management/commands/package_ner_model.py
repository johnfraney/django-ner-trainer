import os
import subprocess
from django.core.management.base import BaseCommand, CommandError

from ner_trainer.conf import settings


class Command(BaseCommand):
    help = 'Packages your custom spaCy model'

    def handle(self, *args, **options):
        model_directory = settings.NER_TRAINER_MODEL_DIRECTORY
        if not os.path.exists(model_directory):
            raise CommandError('Please train a model before packaging')
        if not os.path.exists('dist'):
            os.mkdir('dist')
        subprocess.run(
            ['python', '-m', 'spacy', 'package', model_directory, 'dist', '--create-meta', '--force'],
            check=True
        )
        model_package_dir = os.path.join('dist', os.listdir('dist')[0])
        os.chdir(model_package_dir)
        subprocess.run(['python', 'setup.py', 'sdist'], check=True)
        self.stdout.write(self.style.SUCCESS('Successfully packaged spaCy model'))
