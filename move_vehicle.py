import os
import shutil
import cv2
import tensorflow as tf


model = tf.keras.models.load_model("vehicle_predictor.model")

def prepare(path):
    img_size = 50
    img_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1)



print("Spostamento delle immagini nellg giuste cartelle")

path = "/Users/memex_99/Desktop/Veicoli/VeicoliSelezione"
pathAuto = "/Users/memex_99/Desktop/Veicoli/VeicoliSelezione/AutoSelezione"
pathMoto = "/Users/memex_99/Desktop/Veicoli/VeicoliSelezione/MotoSelezione"


categorie = ["Auto", "Moto"]

photos = os.listdir(path)
for i, p in enumerate(photos):
    if p != ".DS_Store" and p != "AutoSelezione" and p != "MotoSelezione":
        path_photo = os.path.join(path, p)
        prediction = model.predict([prepare(path_photo)])

        print(i, categorie[int(round(prediction[0][0]))])
