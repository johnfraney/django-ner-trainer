# Models

## Entity

`Entity` is the model that puts the 'E' in 'NER'. [spaCy defines an Entity](https://spacy.io/usage/linguistic-features#101) as "a 'real-world object' that's assigned a name – for example, a person, a country, a product or a book title".

#### Fields

* `label` (primary key) - machine-friendly representation of the Entity as used in spaCy
* `name` - user-friendly representation of the Entity

#### Example
```
from ner_trainer.models import Entity

entity = Entity.objects.create(
  label='PROVINCE',
  name='Province'
)
```


## Phrase

`Phrase` is text that may contain zero or more Entities.

#### Fields

* `text` (unique) - phrase text. This field is unique to prevent duplicate Phrases during bulk imports.
* `skipped` - whether the phrase is skipped. Useful when a phrase could be bulk imported more than once.

#### Methods

* `as_spacy_train_data()` - returns a `spacy.gold`-compatible representation of the tagged Phrase:
```
('I like London and Berlin.', {
    'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]
})
```

#### Example
```
from ner_trainer.models import Phrase

phrase = Phrase.objects.create(
  text="Nova Scotia is one of Canada's three maritime provinces."
)
```

#### Custom Managers

* `active_objects` - returns a queryset of all `Phrase` instances that haven't been skipped:

```python
>>> Phrase.active_objects.all() == Phrase.objects.filter(skipped=False)
True
```

* `tagged_objects` - returns a queryset of active `Phrase` instances that have been tagged (i.e., have related `PhraseEntity` objects):

```python
>>> Phrase.tagged_objects.all() == Phrase.objects.filter(skipped=False, entities__isnull=False)
True
```


## PhraseEntity

A `PhraseEntity` joins an `Entity` to a `Phrase` and stores where in the phrase that entity is located.

#### Fields

* `phrase` - `Phrase` containing this named entity
* `entity` - `Entity` defined between `start_index` and `end_index`
* `start_index` - start character index of the `Entity` in the `Phrase`
* `end_index` - end character index of the `Entity` in the `Phrase`

#### Methods

* `as_spacy_tuple()` - returns a tuple of `start_index`, `end_index`, and `entity.label` for use training the spaCy NER model.

