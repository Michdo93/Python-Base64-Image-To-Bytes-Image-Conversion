import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

filename = "/home/ubuntu/testImage"
with open(filename, "rb") as fid:
    data = fid.read()

#b64_bytes = base64.b64encode(data)
b64_bytes = data

#print(b64_bytes)

b64_string = b64_bytes.decode()

#print(b64_string)

print(base64.b64decode(b64_string))

# reconstruct image as an numpy array
img = imread(io.BytesIO(base64.b64decode(b64_string)))

height, width, channels = img.shape
print(height)
print(width)
print(channels)

with open('/home/ubuntu/testImageBytes', 'wb') as file_to_save:
    file_to_save.write(img)
