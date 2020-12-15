import os
import shutil
import cv2
import tensorflow as tf


model = tf.keras.models.load_model("weather_predictor.model")

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


print("Spostamento delle immagini nelle giuste cartelle")

path = "/Users/memex_99/Desktop/Tempo/TempoSelezione"
pathSoleggiato = "/Users/memex_99/Desktop/Tempo/TempoSelezione/SoleggiatoSelezione"
pathCoperto = "/Users/memex_99/Desktop/Opere/TempoSelezione/CopertoSelezione"


categorie = ["Soleggiato", "Coperto"]

photos = os.listdir(path)
for p in photos:
    if p != ".DS_Store" and p != "SoleggiatoSelezione" and p != "CopertoSelezione":
        path_photo = os.path.join(path, p)
        prediction = model.predict([prepare(path_photo)])
        print(categorie[int(prediction[0][0])])
