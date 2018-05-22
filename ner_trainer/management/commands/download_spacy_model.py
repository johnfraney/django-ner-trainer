import subprocess
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Downloads one or more spaCy models'

    def add_arguments(self, parser):
        parser.add_argument('model_code', nargs='+', type=str)

    def handle(self, *args, **options):
        for model_code in options['model_code']:
            try:
                subprocess.run(['python', '-m', 'spacy', 'download', model_code], check=True)
            except subprocess.CalledProcessError:
                raise CommandError('Could not download model "%s"' % model_code)
            self.stdout.write(self.style.SUCCESS('Successfully downloaded model "%s"' % model_code))
