from PIL import Image
from pathlib import Path
import numpy as np
import services.brightness as bright
import services.contrast as contrast 

current_file_directory = Path(__file__).resolve().parent
img_path = current_file_directory / "assets" / "sample.jpg"

img = Image.open(img_path)

img_matrix = np.array(img)

brightness_value = 100
contrast_value = 2.2

bright_img_matrix = bright.adjust_brightness(img_matrix, brightness_value)
contrast_img_matrx = contrast.adjust_contrast(img_matrix, contrast_value)

bright_img = Image.fromarray(bright_img_matrix)
contrast_img = Image.fromarray(contrast_img_matrx)


bright_img.save("bright_result.png")
contrast_img.save("contrast_result.png")

