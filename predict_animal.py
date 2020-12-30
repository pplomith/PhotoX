import cv2
import tensorflow as tf
import os

# quindi ora vogliamo convertire il numero nella stringa
categorie = ["Cane", "Gatto"]


def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("animal_predictor.model")

path = "/Users/memex_99/Desktop/Animali/AnimaliQuestionario"
path_cane = os.path.join(path, "Cane")
path_gatto = os.path.join(path, "Gatto")

print("Classificazione cani")
for i in range(0, 11):
    prediction = model.predict([prepare(os.path.join(path_cane, str(i) + ".jpg"))])
    print(categorie[(int(prediction[0][0]))])

print("\nClassificazione gatti")
for i in range(1, 12):
    prediction = model.predict([prepare(os.path.join(path_gatto, str(i) + ".jpg"))])
    print(categorie[(int(prediction[0][0]))])

