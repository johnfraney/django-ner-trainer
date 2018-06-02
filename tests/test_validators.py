#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-ner-trainer
------------

Tests for `django-ner-trainer` models module.
"""

from django.core.exceptions import ValidationError
from django.test import TestCase

from ner_trainer.validators import validate_all_caps


class TestValidators(TestCase):
    def test_validate_all_caps(self):
        good_label = 'PROVINCE'
        self.assertEqual(validate_all_caps(good_label), None)

        bad_label = 'province'
        with self.assertRaises(ValidationError):
            validate_all_caps(bad_label)
