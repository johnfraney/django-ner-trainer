import os
import subprocess
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Packages your custom SpaCy model'

    def handle(self, *args, **options):
        if not os.path.exists('spacy_model'):
            raise CommandError('Please train a model before packaging')
        if not os.path.exists('dist'):
            os.mkdir('dist')
        subprocess.run(
            ['python', '-m', 'spacy', 'package', 'spacy_model', 'dist', '--create-meta', '--force'],
            check=True
        )
        model_package_dir = os.path.join('dist', os.listdir('dist')[0])
        os.chdir(model_package_dir)
        subprocess.run(['python', 'setup.py', 'sdist'], check=True)
        self.stdout.write(self.style.SUCCESS('Successfully packaged SpaCy model'))
