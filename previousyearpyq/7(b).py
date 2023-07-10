from skimage import io
import numpy as np

image = io.imread("path_to_image.jpg")

image_type = type(image)
print("Image type:", image_type)

image_shape = image.shape
print("Image shape:", image_shape)


# answer asuniii
