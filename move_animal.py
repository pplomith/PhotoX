import os
import shutil
import cv2
import tensorflow as tf


model = tf.keras.models.load_model("animal_predictor.model")

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)



print("Spostamento delle immagini nellg giuste cartelle")

path = "/Users/memex_99/Desktop/Animali/AnimaliSelezione"
pathCani = "/Users/memex_99/Desktop/Opere/AnimaliSelezione/CaniSelezione"
pathGatti = "/Users/memex_99/Desktop/Opere/AnimaliSelezione/GattiSelezione"


categorie = ["Cane", "Gatto"]

photos = os.listdir(path)
for p in photos:
    if p != ".DS_Store" and p != "GattiSelezione" and p != "CaniSelezione":
        path_photo = os.path.join(path, p)
        prediction = model.predict([prepare(path_photo)])
        print(categorie[int(prediction[0][0])])
