import numpy as np
import os
import cv2
import random
import pickle

# numpy per eseguire operazioni sugli array
# matplotplib.pyplot la si usa per mostrare le immagini
# os per gestire le cartelle e i path
# per eseguire operazioni sulle immagini

# ricordiamo che in una classificazione i dati devono essere bilanciati
# vogliamo che il numero di cani eguagli il numero di gatti

# specifichiamo una data directory
DATADIR = "F:/University/IA/Progetto/DataSet/Animali/Animali/PetImages"

# specifichiamo le categorie con le quali eseguire la classificazione
CATEGORIE = ["Dog", "Cat"]

# adesso creiamo il training dataset con tutte le foto della stessa misura

training_data = []
IMG_SIZE = 50


def create_training_data():
    for categoria in CATEGORIE:

        # path ai cani oppure ai gatti
        path = os.path.join(DATADIR, categoria)

        # in questo modo alle immagini associamo le categorie. Perchè le categorie
        # devono essere dei valori numeri
        class_num = CATEGORIE.index(categoria)
        i=0
        for img in os.listdir(path):
            try:
                print("prova ", i)
                # il metodo imread serve per caricare l'immagini dato il path
                # IMREAD_GRAYSCALE serve per dire che deve essere in bianco e nero
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
                i = i+1
            except Exception as e:
                pass

create_training_data()
print(len(training_data))

# necessario per far si che l'addestramento della rete neurale sia diversificato
random.shuffle(training_data)

# lista di features e di label quindi dobbiamo dividere tutto
x_train = []
y_train = []

for features, label in training_data:
    x_train.append(features)
    y_train.append(label)

x_train = np.array(x_train).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y_train = np.array(y_train)

pickle_out = open("x.animal", "wb")
pickle.dump(x_train, pickle_out)
pickle_out.close()

pickle_out = open("y.animal", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()
