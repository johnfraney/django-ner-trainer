# Management Commands

## `download_spacy_model`

Downloads one or more spaCy models. See [spaCy's "Models & Languages" docs](https://spacy.io/usage/models) for more information.

#### Usage

Download one model:

```bash
./manage.py download_spacy_model en_core_web_md
```

Download multiple models:
```bash
./manage.py download_spacy_model en de fr
```


## `train_ner_model`

Trains your custom spaCy model using settings specified in your project configuration. See [spaCy's "Training the named entity recognizer" docs](https://spacy.io/usage/training#section-ner) for more information.

#### Settings

```
NER_TRAINER_MODEL_DIRECTORY
NER_TRAINER_MODEL_NAME
NER_TRAINER_MODEL_TRAIN_ITERATIONS
```

#### Usage

```bash
./manage.py train_ner_model
```


## `package_ner_model`

Packages your custom spaCy model. See [spaCy's "Generating a model package" docs](https://spacy.io/usage/training#models-generating) for more information.

#### Usage

```bash
./manage.py package_ner_model
```

#### Settings

```
NER_TRAINER_MODEL_DIRECTORY
```

