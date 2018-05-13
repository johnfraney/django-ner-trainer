=====
Usage
=====

To use Django NER Trainer in a project, add it to your `INSTALLED_APPS`:

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
