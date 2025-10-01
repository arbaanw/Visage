import numpy as np

def adjust_contrast(img_matrix, contrast_value):
    output_img_matrix =(img_matrix * contrast_value).astype('uint8')
    np.clip(output_img_matrix, 0, 255)
    return output_img_matrix

