# Adapted from https://github.com/carltongibson/django-filter/blob/master/django_filters/conf.py
from django.conf import settings as dj_settings
from django.core.signals import setting_changed

SETTINGS_PREFIX = 'NER_TRAINER_'

DEFAULTS = {
    'NER_TRAINER_MODEL_DIRECTORY': 'spacy_model',
    'NER_TRAINER_MODEL_NAME': 'ner_model',
    'NER_TRAINER_MODEL_TRAIN_ITERATIONS': 20,
}


def is_callable(value):
    # check for callables, except types
    return callable(value) and not isinstance(value, type)


class Settings(object):

    def __getattr__(self, name):
        if name not in DEFAULTS:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (self.__class__.__name__, name))

        value = self.get_setting(name)

        if is_callable(value):
            value = value()

        # Cache the result
        setattr(self, name, value)
        return value

    def get_setting(self, setting):
        django_setting = '{}{}'.format(SETTINGS_PREFIX, setting)

        return getattr(dj_settings, django_setting, DEFAULTS[setting])

    def change_setting(self, setting, value, enter, **kwargs):
        if not setting.startswith(SETTINGS_PREFIX):
            return
        setting = setting[len(SETTINGS_PREFIX):]  # strip SETTINGS_PREFIX

        # ensure a valid app setting is being overridden
        if setting not in DEFAULTS:
            return

        # if exiting, delete value to repopulate
        if enter:
            setattr(self, setting, value)
        else:
            delattr(self, setting)


settings = Settings()
setting_changed.connect(settings.change_setting)
