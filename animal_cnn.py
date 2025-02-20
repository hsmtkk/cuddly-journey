import pickle

import numpy
import tensorflow as tf
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
    Activation,
)

classes = ["monkey", "parrot", "rabbit"]
num_classes = len(classes)
image_size = 50


def main():
    with open("animal.pkl", "rb") as f:
        xy = pickle.load(f)
        X_train = xy[0]
        X_test = xy[1]
        y_train = xy[2]
        y_test = xy[3]

    X_train = X_train.astype("float") / 256.0
    X_test = X_test.astype("float") / 256.0
    y_train = tf.keras.utils.to_categorical(y_train, num_classes)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes)

    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)


def model_train(X: numpy.ndarray, y: numpy.ndarray) -> tf.keras.models.Sequential:
    model = tf.keras.models.Sequential()
    model.add(
        Conv2D(32, (3, 3), padding="same", input_shape=(image_size, image_size, 3))
    )
    model.add(Activation("relu"))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation("softmax"))

    opt = tf.keras.optimizers.RMSprop(learning_rate=1e-3)
    model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

    model.fit(X, y, batch_size=32, epochs=10)

    model.save("./animal_cnn.keras")

    return model


def model_eval(
    model: tf.keras.models.Sequential, X_test: numpy.ndarray, y_test: numpy.ndarray
):
    scores = model.evaluate(X_test, y_test, verbose=1)
    print("Test Loss: ", scores[0])
    print("Test Accuracy: ", scores[1])


if __name__ == "__main__":
    main()
