import numpy as np

# A class to generate and hold a binary-valued array from an input picture.
# Construction requires a Pillow Image object as an argument.
# Call ArrayFromPic.mapped_array to get array.


class ArrayFromPic1:

    def __init__(self, im):

        width = im.size[0]
        height = im.size[1]
        data = list(im.getdata(1))

        self.mapped_array = np.zeros((width, height))
        index_count = 0
        row = 0
        column = 0
        for x in data:
            if x < 255:
                self.mapped_array[row][column] = 1
            index_count += 1
            column += 1
            if index_count % width == 0:
                row += 1
                column = 0