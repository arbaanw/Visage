import numpy as np

def inversion(img_matrix):
    output_img_matrix = np.copy(img_matrix)
    for index, value in np.ndenumerate(output_img_matrix):
        output_img_matrix[index] = 255 - value
    return output_img_matrix
