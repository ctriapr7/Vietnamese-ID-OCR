#Choose python 3.9
from PIL import Image   
from imutils.contours import sort_contours
import numpy as np
import pytesseract
import argparse
import imutils
import sys
import cv2 as cv 

#image_test = Image.open("/Users/hoangcongtri/Desktop/CS/Python/OCR /CCCD/cccd1.jpeg")
#cccd1 = "image_1.jpeg"
image_test_1 = Image.open("cc1.jpeg")
print(pytesseract.image_to_string(image_test_1, config='-l vie' ))

#locating 4 corners of the ID using openCV
