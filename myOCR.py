import numpy as np
from sklearn.naive_bayes import GaussianNB

from processImage import process_image
from utilFunctions import mtx_to_array

img_size = (15, 15)
training_size_single_letter = 10
num_letters = 5
im = process_image('L/L1.png', size=img_size)
ax = np.asarray(im)

training = np.zeros((training_size_single_letter * num_letters, ax.shape[0] * ax.shape[1]))
labels = np.empty(training_size_single_letter * num_letters, dtype='string')


def get_training_images(letter, im_size, t_size=10, starting_index=0):
    for itr in range(1, t_size + 1):
        im_as_arr = np.asarray(process_image(letter + '/' + letter + str(itr) + '.png', size=im_size))
        mtx_as_arr = mtx_to_array(im_as_arr)
        training[starting_index + itr - 1] = mtx_as_arr
        labels[starting_index + itr - 1] = letter


get_training_images('L', img_size, starting_index=0)
get_training_images('A', img_size, starting_index=10)
get_training_images('B', img_size, starting_index=20)
get_training_images('X', img_size, starting_index=30)
get_training_images('O', img_size, starting_index=40)

clf = GaussianNB()
clf = clf.fit(training, labels)

for ti in range(1, 9):
    print clf.predict([mtx_to_array(np.asarray(process_image('test/t' + str(ti) + '.png', size=img_size)))])
