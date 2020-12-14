import numpy as np
import pickle
import cv2
import random
import os

datadir = "F:/University/IA/Progetto/DataSet/Tempo/Tempo"
img_size = 120
categorie = ["Soleggiato", "Coperto"]

training_data = []


def create_training_data():
    for categoria in categorie:

        path = os.path.join(datadir, categoria)
        i = 0
        class_num = categorie.index(categoria)

        for img in os.listdir(path):
            try:
                print(i)
                i += 1
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                new_array = cv2.resize(img_array, (img_size, img_size))
                new_array = modify(new_array, new_array.shape)

                training_data.append([new_array, class_num])

            except Exception as e:
                pass


def modify(img_src, img_shape):
    shape = img_shape

    for i in range(shape[0]):
        for j in range(shape[1]):
            for z in range(shape[2]):
                if img_src[i, j, z] < 155:
                    img_src[i, j, z] = 0

    return img_src


create_training_data()
random.shuffle(training_data)

x_train = []
y_train = []

for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

x_train = np.array(x_train).reshape(-1, img_size, img_size, 3)
y_train = np.array(y_train)

pickle_out = open("x.weather", "wb")
pickle.dump(x_train, pickle_out)
pickle_out.close()

pickle_out = open("y.weather", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()
