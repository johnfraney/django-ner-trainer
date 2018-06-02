from django.test import TestCase
from ner_trainer.forms import ModelTestForm


class ModelTestFormTests(TestCase):
    def test_invalid_model_test_form(self):
        """
        Ensure a ModelTestForm instance without text is invalid.
        """
        form = ModelTestForm()
        self.assertFalse(form.is_valid())

    def test_valid_model_test_form(self):
        """
        Ensure a ModelTestForm instance with text is valid.
        """
        form = ModelTestForm({'text': 'This is a sentence'})
        self.assertTrue(form.is_valid())
