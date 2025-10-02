import numpy as np

def adjust_brightness(img_matrix, brightness_value):
    brightness_matrix = np.full(img_matrix.shape, brightness_value)
    output_img_matrix = (np.clip((img_matrix + brightness_matrix), 0, 255)).astype("uint8")
    return output_img_matrix
