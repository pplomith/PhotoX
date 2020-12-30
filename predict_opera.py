import cv2
import tensorflow as tf
import os

categorie = ["Quadro", "Scultura"]


def prepare(path_image):
    img_size = 100
    img_array = cv2.imread(path_image, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    edges = cv2.Canny(new_array, 1, 255)
    return edges.reshape(-1, img_size, img_size, 1)


model = tf.keras.models.load_model("opera_predictor.model")

path = "/Users/memex_99/Desktop/Opere/OpereQuestionario"
path_quadro = os.path.join(path, "Quadro")
path_scultura = os.path.join(path, "Scultura")

print("Predizione quadri")
for i in range(1, 11):
    prediction = model.predict([prepare(os.path.join(path_quadro, str(i) + ".jpg"))])
    print(categorie[int(prediction[0][0])])

print("\nPredizione sculture")
for i in range(1, 11):
    prediction = model.predict([prepare(os.path.join(path_scultura, str(i) + ".jpg"))])
    print(categorie[int(prediction[0][0])])
