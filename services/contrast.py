import numpy as np

def adjust_contrast(img_matrix, contrast_value):
    output_img_matrix = np.copy(img_matrix)
    for index, value in np.ndenumerate(output_img_matrix):
        if 0 <= 128 + (value - 128) * contrast_value <= 255:
            output_img_matrix[index] = 128 + (value - 128) * contrast_value
    return(output_img_matrix)

