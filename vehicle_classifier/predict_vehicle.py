import cv2
import tensorflow as tf

categorie = ["Auto", "Moto"]


def prepare(path):
    img_size = 50
    img_array = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 1)


model = tf.keras.models.load_model("vehicle_predictor.model")

path = "F:/University/IA/Progetto/DataSet/Cars"
path_moto = path + "/Moto/"
path_auto = path + "/Auto/"


print("Predizione auto")
for i in range(1, 11):
    prediction = model.predict([prepare(path_auto + str(i) + ".jpg")])
    print(categorie[int(round(prediction[0][0]))])


print("Predizione moto")
for i in range(1, 11):
    prediction = model.predict([prepare(path_moto + str(i) + ".jpeg")])
    print(categorie[int(round(prediction[0][0]))])
