# # used to process a character image # loads a given character image, crops to the exact size of the character,
# convert to black and white image and resize to a size and returns
import numpy as np
from PIL import Image, ImageOps


def process_image(file_name, size=(7, 7)):
    img = Image.open(file_name)

    out_img = img.convert('L')
    out_img = ImageOps.invert(out_img)

    # out_img.show()

    np_array = np.asarray(out_img)

    rowSum = np.sum(np_array, 0)

    columnSum = np.sum(np_array, 1)

    def find_left(row_sum):
        for i in range(row_sum.shape[0]):
            if row_sum[i] > 0:
                return i

    def find_right(row_sum):
        for i in range(row_sum.shape[0] - 1, 0, -1):
            if row_sum[i] > 0:
                return i

    def find_top(column_sum):
        for i in range(column_sum.shape[0]):
            if column_sum[i] > 0:
                return i

    def find_bottom(column_sum):
        for i in range(column_sum.shape[0] - 1, 0, -1):
            if column_sum[i] > 0:
                return i

    left = find_left(rowSum)
    right = find_right(rowSum)
    top = find_top(columnSum)
    bottom = find_bottom(columnSum)

    box = (left, top, right, bottom)
    cropped_img = out_img.crop(box)

    # cropped.show()

    resize_img = cropped_img.resize(size, Image.LANCZOS)

    # transf.show()
    # transf.convert('1').show()

    def convert_bw(im, threshold=50):
        ta = np.asarray(im)
        tt = np.array(ta, copy=True)

        for i in range(tt.shape[0]):
            for j in range(tt.shape[1]):
                if tt[i][j] > threshold:
                    tt[i][j] = 255
                else:
                    tt[i][j] = 0

        tti = Image.fromarray(tt)
        return tti

    return convert_bw(resize_img, 50)
