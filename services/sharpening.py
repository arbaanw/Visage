import numpy as np

kernel = np.array([[ 0,   -0.25,  0],
                   [-0.25, 1.5, -0.25],
                   [ 0,   -0.25, 0]])

def effect_sharpening(img_matrix):
    h, w = img_matrix.shape[:2]
    output_img_matrix = img_matrix.astype("float32")
    padded = np.pad(output_img_matrix, ((1, 1), (1, 1), (0,0)), mode ="edge")
    for c in range(3):
        for indices, _ in np.ndenumerate(output_img_matrix[:, :, c]):
            x = indices[0] + 1
            y = indices[1] + 1
            output_img_matrix[indices[0], indices[1], c] = np.sum((padded[x-1: x+2, y-1: y+2, c])*kernel)

    return output_img_matrix.astype("uint8")
