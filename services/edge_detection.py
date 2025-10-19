import numpy as np 
import math 

def find_average(arr):
    return arr[0]*0.299+arr[1]*0.587+arr[2]*0.114


def effect_edge_detection(img_matrix):
    output_img_matrix = np.copy(img_matrix)
    padded = np.pad(output_img_matrix, ((1,1), (1,1), (0,0)), mode = "edge")
    G_list = []
    for x in range(output_img_matrix.shape[0]):
        for y in range(output_img_matrix.shape[1]):
            Gx = find_average(padded[x+2, y]) - find_average(padded[x, y])
            Gy = find_average(padded[x, y+2]) - find_average(padded[x, y])

            G = math.sqrt((Gx**2) + (Gy **2))
            G_list.append(G)
    Gmax = max(G_list)
    T = Gmax * 0.2

    for x in range(output_img_matrix.shape[0]):
        for y in range(output_img_matrix.shape[1]):
            Gx = find_average(padded[x+2, y]) - find_average(padded[x, y])
            Gy = find_average(padded[x, y+2]) - find_average(padded[x, y])
            G = math.sqrt((Gx**2) + (Gy **2))

            if G>T:
                output_img_matrix[x, y] = [255, 255, 255]
            else:
                output_img_matrix[x,y] = [0, 0, 0]

    return output_img_matrix
