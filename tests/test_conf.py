from django.test import TestCase

from ner_trainer.conf import settings, DEFAULTS


class SettingsTests(TestCase):
    def test_default_settings(self):
        for setting_name, default_value in DEFAULTS.items():
            self.assertEqual(getattr(settings, setting_name), default_value)

    def test_nonexistant_setting(self):
        with self.assertRaises(AttributeError):
            settings.BANANA
