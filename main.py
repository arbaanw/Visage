from PIL import Image
from pathlib import Path
import numpy as np
import services.brightness as bright
import services.contrast as contrast 
import services.inversion as inversion
import services.thresholding as thresholding
import services.blurring as blurring
import services.edge_detection as edge

current_file_directory = Path(__file__).resolve().parent
img_path = current_file_directory / "assets" / "mona_lisa"

img = Image.open(img_path)

img_matrix = np.array(img)

brightness_value = 100
contrast_value = 1.8

bright_img_matrix = bright.effect_brightness(img_matrix, brightness_value)
contrast_img_matrix = contrast.effect_contrast(img_matrix, contrast_value)
inversion_img_matrix = inversion.effect_inversion(img_matrix)
thresholding_img_matrix = thresholding.effect_thresholding(img_matrix)
blurring_img_matrix = blurring.effect_blurring(img_matrix)
edge_img_matrix = edge.effect_edge_detection(img_matrix)


bright_img = Image.fromarray(bright_img_matrix)
contrast_img = Image.fromarray(contrast_img_matrix)
inversion_img = Image.fromarray(inversion_img_matrix)
thresholding_img = Image.fromarray(thresholding_img_matrix)
blurring_img = Image.fromarray(blurring_img_matrix)
edge_img = Image.fromarray(edge_img_matrix)


bright_img.save("results/bright_result.png")
contrast_img.save("results/contrast_result.png")
inversion_img.save("results/inversion_result.png")
thresholding_img.save("results/thresholding_result.png")
blurring_img.save("results/blurring_result.png")
edge_img.save("results/edge_detection_result.png")
