=============================
Django NER Trainer
=============================

.. image:: https://badge.fury.io/py/django-ner-trainer.svg
    :target: https://badge.fury.io/py/django-ner-trainer

.. image:: https://travis-ci.org/johnfraney/django-ner-trainer.svg?branch=master
    :target: https://travis-ci.org/johnfraney/django-ner-trainer

.. image:: https://codecov.io/gh/johnfraney/django-ner-trainer/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/johnfraney/django-ner-trainer

Tools for training spaCy Named Entity Recognition models in Django

Documentation
-------------

The full documentation is at https://django-ner-trainer.readthedocs.io.

Quickstart
----------

Install Django NER Trainer::

    pip install django-ner-trainer

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ner_trainer.apps.NerTrainerConfig',
        ...
    )

Add Django NER Trainer's URL patterns:

.. code-block:: python

    from ner_trainer import urls as ner_trainer_urls


    urlpatterns = [
        ...
        url(r'^', include(ner_trainer_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
