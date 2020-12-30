import os
import shutil
import cv2
import tensorflow as tf


model = tf.keras.models.load_model("opera_predictor.model")

def prepare(path_image):
    img_size = 100
    img_array = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    edges = cv2.Canny(new_array, 5, 255)
    return edges.reshape(-1, img_size, img_size, 1)


path = "/Users/memex_99/Desktop/Opere/OpereSelezione"
pathQuadri = "/Users/memex_99/Desktop/Opere/OpereSelezione/QuadriSelezione"
pathSculture = "/Users/memex_99/Desktop/Opere/OpereSelezione/ScultureSelezione"

categorie = ["Quadro", "Scultura"]

photos = os.listdir(path)
for p in photos:
    if p != ".DS_Store" and p != "ScultureSelezione" and p != "QuadriSelezione":
        path_photo = os.path.join(path, p)
        prediction = model.predict([prepare(path_photo)])

        if categorie[int(prediction[0][0])] == "Quadro":
            shutil.copy(path_photo, os.path.join(pathQuadri, p))
        else:
            shutil.copy(path_photo, os.path.join(pathSculture, p))
