import numpy as np

def find_average(arr):
    return arr[0]*0.299+arr[1]*0.587+arr[2]*0.114

def effect_thresholding(img_matrix):
    T = 127
    output_img_matrix = np.copy(img_matrix)
    for x in range(output_img_matrix.shape[0]):
        for y in range(output_img_matrix.shape[1]):
            average_value = find_average(output_img_matrix[x, y])
            if average_value > T:
                output_img_matrix[x,y] = [255, 255, 255]
            else:
                output_img_matrix[x, y] = [0, 0, 0]

    return output_img_matrix
