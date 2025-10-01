import numpy as np

def adjust_brightness(img_matrix, brightness_value):
    brightness_matrix = np.full(img_matrix.shape, brightness_value)
    np.clip(brightness_matrix, 0, 255)
    output_img_matrix = (img_matrix + brightness_matrix).astype("uint8")
    return output_img_matrix
