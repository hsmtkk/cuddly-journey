import glob
import pickle

import numpy
from PIL import Image

classes = ["monkey", "parrot", "rabbit"]
num_classes = len(classes)
target_image_size = 50
num_test_data = 100

X_train = []
X_test = []
y_train = []
y_test = []

for index, cls in enumerate(classes):
    photos_dir = "./" + cls
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((target_image_size, target_image_size))
        data = numpy.asarray(image)
        if i < num_test_data:
            X_test.append(data)
            y_test.append(index)
        else:
            for angle in range(-20, 20, 5):
                img_r = image.rotate(angle)
                data = numpy.asarray(img_r)
                X_train.append(data)
                y_train.append(index)

                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = numpy.asarray(img_trans)
                X_train.append(data)
                y_train.append(index)

X_train = numpy.array(X_train)
X_test = numpy.array(X_test)
y_train = numpy.array(y_train)
y_test = numpy.array(y_test)

xy = (X_train, X_test, y_train, y_test)

with open("animal.pkl", "wb") as f:
    pickle.dump(xy, f)

with open("animal.pkl", "rb") as f:
    xy = pickle.load(f)
