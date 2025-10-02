from PIL import Image
from pathlib import Path
import numpy as np
import services.brightness as bright
import services.contrast as contrast 
import services.inversion as inversion

current_file_directory = Path(__file__).resolve().parent
img_path = current_file_directory / "assets" / "sample.jpg"

img = Image.open(img_path)

img_matrix = np.array(img)

brightness_value = 100
contrast_value = 1.8

bright_img_matrix = bright.adjust_brightness(img_matrix, brightness_value)
contrast_img_matrix = contrast.adjust_contrast(img_matrix, contrast_value)
inversion_img_matrix = inversion.inversion(img_matrix)

bright_img = Image.fromarray(bright_img_matrix)
contrast_img = Image.fromarray(contrast_img_matrix)
inversion_img = Image.fromarray(inversion_img_matrix)

bright_img.save("results/bright_result.png")
contrast_img.save("results/contrast_result.png")
inversion_img.save("results/inversion_result.png")
