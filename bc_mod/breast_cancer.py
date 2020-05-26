import tensorflow 
import numpy as np 

def get_model():
    global model
    model =tensorflow.keras.models.load_model('bc_mod/breast_cancer_model.h5')
    model._make_predict_function()
    

def predict_class(IMG):
    img_path = IMG
    img = tensorflow.keras.preprocessing.image.load_img(img_path, target_size=(224,224))
    x = tensorflow.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    model_class =  np.argmax(model.predict(x), axis=-1)
    return model_class

def predict_accuracy(IMG):
    img_path = IMG
    img = tensorflow.keras.preprocessing.image.load_img(img_path, target_size=(224,224))
    x = tensorflow.keras.preprocessing.image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    accuracy =  model.predict(x)
    model_accuracy = np.max(accuracy)*100
    return model_accuracy