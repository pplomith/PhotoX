import cv2
import tensorflow as tf

categorie = ["Auto", "Moto"]


def prepare(path):
    img_size = 50
    img_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1)


model = tf.keras.models.load_model("vehicle_predictor.model")

path = "/Users/memex_99/Desktop/Veicoli/VeicoliQuestionario/"
path_moto = path + "/Moto/"
path_auto = path + "/Auto/"


print("Predizione auto")
for i in range(0, 11):
    prediction = model.predict([prepare(path_auto + str(i) + ".jpg")])
    print(categorie[int(prediction[0][0])])


print("Predizione moto")
for i in range(0, 10):
    prediction = model.predict([prepare(path_moto + str(i) + ".jpg")])
    print(categorie[int(prediction[0][0])])
