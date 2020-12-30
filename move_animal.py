import os
import shutil
import cv2
import tensorflow as tf

model = tf.keras.models.load_model("animal_predictor.model")


def prepare(filepath):
    img_size = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1)


path = "/Users/memex_99/Desktop/Animali/AnimaliSelezione"
pathCani = "/Users/memex_99/Desktop/Animali/AnimaliSelezione/CaniSelezione"
pathGatti = "/Users/memex_99/Desktop/Animali/AnimaliSelezione/GattiSelezione"

categorie = ["Cane", "Gatto"]

photos = os.listdir(path)
for p in photos:
    if p != ".DS_Store" and p != "GattiSelezione" and p != "CaniSelezione":
        path_photo = os.path.join(path, p)
        prediction = model.predict([prepare(path_photo)])

        print(prediction[0][0], p)

        if categorie[int(prediction[0][0])] == "Cane":
            shutil.copy(path_photo, os.path.join(pathCani, p))
        else:
            shutil.copy(path_photo, os.path.join(pathGatti, p))

