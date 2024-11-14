import glob
import pickle

import numpy
from PIL import Image
import sklearn.model_selection

classes = ["monkey", "parrot", "rabbit"]
num_classes = len(classes)
target_image_size = 50

X = []
y = []

for index, cls in enumerate(classes):
    photos_dir = "./" + cls
    files = glob.glob(photos_dir + "/*.jpg")
    for i, file in enumerate(files):
        image = Image.open(file)
        image = image.convert("RGB")
        image = image.resize((target_image_size, target_image_size))
        data = numpy.asarray(image)
        X.append(data)
        y.append(index)

X = numpy.array(X)
y = numpy.array(y)

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2, random_state=0
)

# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

xy = (X_train, X_test, y_train, y_test)

with open("animal.pkl", "wb") as f:
    pickle.dump(xy, f)

with open("animal.pkl", "rb") as f:
    xy = pickle.load(f)
