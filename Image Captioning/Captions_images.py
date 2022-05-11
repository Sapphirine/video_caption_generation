#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from numpy import argmax
from pickle import load
from keras.models import load_model
from nltk.translate.bleu_score import corpus_bleu


# In[ ]:


from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


# In[ ]:


def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


# In[ ]:


def load_set(filename):
    doc = load_doc(filename)
    dataset = list()
    # process line by line
    for line in doc.split('\n'):
        # skip empty lines
        if len(line) < 1:
            continue
        # get the image identifier
        identifier = line.split('.')[0]
        dataset.append(identifier)
    return set(dataset)


# In[ ]:




