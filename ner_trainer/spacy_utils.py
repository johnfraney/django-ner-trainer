"""
Example of training an additional entity type

Adapted from official spaCy 2.0.x example:
https://github.com/explosion/spaCy/blob/v2.0.2/examples/training/train_ner.py

"""
import multiprocessing
from pathlib import Path
import random
import spacy


def train_ner(entity_labels, train_data, model_directory, model_name, n_iter=20, device=0, drop=0.35):
    nlp = spacy.blank('en')  # create blank Language class

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    # Add new entities to model
    for label in entity_labels:
        ner.add_label(label)

    # Get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        cpu_count = multiprocessing.cpu_count()  # make use of all CPU threads
        optimizer = nlp.begin_training(n_threads=cpu_count, device=device)
        for itn in range(n_iter):
            random.shuffle(train_data)
            losses = {}
            for text, annotations in train_data:
                nlp.update([text], [annotations], sgd=optimizer, drop=drop,
                           losses=losses)
            print(losses)

    output_dir = Path(model_directory)
    if output_dir:
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to ", output_dir)
