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
b64_string = b64_bytes.decode()

bytes_string = base64.b64decode(b64_string)

jpg_as_text = str(bytes_string)

text_file = open("testImageBytes3", "w")
 
#write string to file
text_file.write(jpg_as_text)
 
#close file
text_file.close()
