# author: sbaidya
# date: 08.04.2021

import cv2  # importing opencv
from PIL import Image  # importing pillow # to store image objects
import pytesseract
import func
from func import *

'''
List of available languages
I've already preconfigured indic languages with the installation
'''
# print(pytesseract.get_languages(config=''))

image_file = "data/sanskrit/files/page-9.jpeg"
cv2.namedWindow("output", cv2.WINDOW_NORMAL)  # Create window with freedom of dimensions
# cv2.resizeWindow("output", 400, 300) # constant dimension
img = cv2.imread(image_file)
# we can define the crop parameter once for the same book. Most of the pages will be positioned same.
crop_img = func.crop(img, 170, 170, 2050, 1450)  # crop parameters
# bold_font_image = functions.dilation(crop_img) # changing font boldness
test_image_temp = func.remove_noise(crop_img, 1, 4)
cv2.imwrite("processed_data/without_noise.jpeg", test_image_temp)
test_image = func.dilation(test_image_temp, 2)
cv2.imwrite("processed_data/dilated_image.jpeg", test_image)

cv2.imshow("output", test_image) # for viewing only # close the window for further processing
cv2.waitKey(0)

# comparing result
ocr = pytesseract.image_to_string(test_image, lang='san')

with open("output/output-page-9.txt", "w", encoding="utf-8") as text_file:
    text_file.write(ocr)

print(ocr)