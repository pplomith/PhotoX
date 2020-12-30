import pickle

from functions import plot_learning_curve
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D


x = pickle.load(open("x.opera", "rb"))
y = pickle.load(open("y.opera", "rb"))

x = x / 255.0

model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=x.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(64))
model.add(Activation("relu"))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(x, y, batch_size=32, epochs=3, validation_split=0.1)

model.save("opera_predictor.model")

plot_learning_curve(history)
