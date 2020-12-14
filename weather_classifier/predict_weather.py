import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt

categorie = ["Soleggiato", "Coperto"]


def prepare(path_image):
    img_size = 120

    img_array = cv2.imread(path_image, cv2.IMREAD_UNCHANGED)
    new_array = cv2.resize(img_array, (img_size, img_size))

    shape = new_array.shape

    for i in range(shape[0]):
        for j in range(shape[1]):
            for z in range(shape[2]):
                if new_array[i, j, z] < 155:
                    new_array[i, j, z] = 0

    plt.imshow(new_array)
    plt.show()

    return new_array.reshape(-1, img_size, img_size, 3)


model = tf.keras.models.load_model("weather_predictor.model")

path = "F:/University/IA/Progetto/DataSet/Tempo/Tempo/TempoQuestionario"
path_soleggiato = os.path.join(path, "Soleggiato")
path_coperto = os.path.join(path, "Coperto")

print("Predizione soleggiato")
for i in range(1, 11):
    prediction = model.predict([prepare(os.path.join(path_soleggiato, str(i) + ".jpg"))])
    print(categorie[int(round(prediction[0][0]))])

print("Predizione coperto")
for i in range(1, 11):
    prediction = model.predict([prepare(os.path.join(path_coperto, str(i) + ".jpg"))])
    print(categorie[int(round(prediction[0][0]))])
