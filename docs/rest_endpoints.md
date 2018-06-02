# REST Endpoints

`django-ner-trainer` ships with REST endpoints using the excellent [Django REST Framework](http://www.django-rest-framework.org/).

Every endpoint save `test-ner/` is a Django REST Framework ViewSet. See the [DRF docs on ViewSets](http://www.django-rest-framework.org/api-guide/viewsets/) for more information


## `entities/`
`Entity` ViewSet

## `phrases/`
`Phrase` ViewSet

### `phrases/active/`
List of Phrases that haven't been skipped.

### `phrases/tagged/`
List of active Phrases that have been tagged (i.e., have `PhraseEntity` objects associated with them).

## `phrase_entities/`

`PhraseEntity` ViewSet

## `test-ner/`
`POST` endpoint that accepts a `text` parameter and returns text tagged using your NER model.
