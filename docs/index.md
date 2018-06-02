# Introduction

`django-ner-trainer` is a set of Django models, management commands, and REST endpoints to help make it easier to train spaCy Named Entity Recognition models within Django.

**N.B.** This package is designed to provide the minimum backend infrastructure you need to train an NER model. It isn't meant to be a full-featured application like [Prodigy](https://prodi.gy/). In other words, this plugin is bring-your-own-front-end.

## Quickstart

Install Django NER Trainer:

```bash
pip install django-ner-trainer
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'ner_trainer',
    ...
)
```

Add Django NER Trainer's URL patterns:

```python
from ner_trainer import urls as ner_trainer_urls


urlpatterns = [
    ...
    url(r'^', include(ner_trainer_urls)),
    ...
]
```

## Features

* [Management commands](management_commands.md) to download spaCy models, training a NER model, and packaging a NER model
* [Models](models.md) for storing phrases, entities, and tagged phrase entities
* [REST Endpoints](rest_endpoints.md) for performing CRUD actions on relevant models

## Running Tests

Does the code actually work?

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```
