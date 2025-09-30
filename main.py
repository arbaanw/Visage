from PIL import Image
from pathlib import Path
import numpy as np

current_file_directory = Path(__file__).resolve().parent
img_path = current_file_directory / "assets" / "images" / "013f753700534f854dfdea8c510d16b0.jpg"

img = Image.open(img_path)

img_matrix = np.array(img)
print(img_matrix)
