#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pickle import load
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from keras.models import load_model


# In[ ]:


# extract features from each photo in the directory
def extract_features(filename):
    
    model = VGG16()
    model.layers.pop()
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    image = load_img(filename, target_size=(224, 224))
   
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
   
    image = preprocess_input(image)
    feature = model.predict(image, verbose=0)
    return feature


# In[ ]:



tokenizer = load(open('tokenizer.pkl', 'rb'))
max_length = 33
model = load_model('model_4.h5')


# In[ ]:


photo = extract_features('frame.jpg')
description = generate_desc(model, tokenizer, photo, max_length)
print(description)

