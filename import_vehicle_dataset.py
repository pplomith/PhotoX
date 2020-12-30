import numpy as np
import os
import cv2
import random
import pickle

datadir = "/Users/memex_99/Desktop/Veicoli/ImmaginiVeicoli"
categorie = ["Auto", "Moto"]

training_data = []

img_size = 50


def create_training_data():
    for categoria in categorie:

        path = os.path.join(datadir, categoria)

        class_num = categorie.index(categoria)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_num])

            except Exception as e:
                pass

create_training_data()
random.shuffle(training_data)

x_train = []
y_train = []

for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

x_train = np.array(x_train).reshape(-1, img_size, img_size, 1)
y_train = np.array(y_train)

pickle_out = open("x.vehicle", "wb")
pickle.dump(x_train, pickle_out)
pickle_out.close()

pickle_out = open("y.vehicle", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()
