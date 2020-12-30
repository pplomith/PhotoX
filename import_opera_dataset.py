import numpy as np
import os
import cv2
import random
import pickle
import matplotlib.pyplot as plt


datadir = "/Users/memex_99/Desktop/Opere/ImmaginiOpere"
img_size = 100
categorie = ["Quadro", "Scultura"]

img_array_quadro = cv2.imread(os.path.join(datadir, "Quadro/0079.jpg"), cv2.IMREAD_GRAYSCALE)
new_array_quadro = cv2.resize(img_array_quadro, (img_size, img_size))
edges_quadro = cv2.Canny(new_array_quadro, 5, 255)

img_array_scultura = cv2.imread(os.path.join(datadir, "Scultura/243.jpg"), cv2.IMREAD_GRAYSCALE)
new_array_scultura = cv2.resize(img_array_scultura, (img_size, img_size))
edges_scultura = cv2.Canny(new_array_scultura, 5, 255)

plt.imshow(edges_quadro, cmap="gray")
plt.show()
plt.imshow(edges_scultura, cmap="gray")
plt.show()

training_data = []

def create_training_data():
    for categoria in categorie:

        path = os.path.join(datadir, categoria)

        class_num = categorie.index(categoria)

        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (img_size, img_size))
                edges = cv2.Canny(new_array, 5, 255)
                training_data.append([edges, class_num])

            except Exception as e:
                pass

    return training_data


create_training_data()
random.shuffle(training_data)

x_train = []
y_train = []

for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

x_train = np.array(x_train).reshape(-1, img_size, img_size, 1)
y_train = np.array(y_train)


pickle_out = open("x.opera", "wb")
pickle.dump(x_train, pickle_out)
pickle_out.close()

pickle_out = open("y.opera", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()
