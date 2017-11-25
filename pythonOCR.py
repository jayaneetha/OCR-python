import numpy as np
from sklearn.naive_bayes import GaussianNB

from processImage import process_image

img_size = (15, 15)
training_size_single_letter = 10
num_letters = 5
im = process_image('L/L1.png', size=img_size)
ax = np.asarray(im)

training_set = np.empty((training_size_single_letter * num_letters, img_size[0] * img_size[1]))

label_set = np.empty(training_size_single_letter * num_letters, dtype='string')


def get_training_images(letter, im_size, starting_index=0):
    for itr in range(1, training_size_single_letter + 1):
        im_as_arr = np.asarray(process_image(letter + '/' + letter + str(itr) + '.png', size=im_size))

        im_as_vector = np.concatenate(im_as_arr)

        training_set[starting_index + itr - 1] = im_as_vector
        label_set[starting_index + itr - 1] = letter


get_training_images('L', img_size, starting_index=0)
get_training_images('A', img_size, starting_index=10)
get_training_images('B', img_size, starting_index=20)
get_training_images('X', img_size, starting_index=30)
get_training_images('O', img_size, starting_index=40)

clf = GaussianNB()
clf = clf.fit(training_set, label_set)

for ti in range(1, 9):
    img = process_image('test/t' + str(ti) + '.png', size=img_size)
    img_vector = np.concatenate(np.asarray(img))

    print clf.predict([img_vector])
