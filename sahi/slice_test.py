
import cv2
import numpy as np
from slicing import slice_image
import sys
sys.path.append('/Users/jerryw/Desktop/code/pytorch/sahi')


image = cv2.imread("/Users/jerryw/Desktop/000001.png")
slices = slice_image(image)

print(slices.image_dir)