import numpy as np

def thresholding(img_matrix):
    t = 127
    output_img_matrix = np.copy(img_matrix)
    for index, value in np.ndenumerate(output_img_matrix):
        output_img_matrix[index] = 255 if value > t else 0

    return output_img_matrix
