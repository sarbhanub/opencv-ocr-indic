# author: sbaidya
# date: 08.05.2021
# for the index structure
# took some techniques from stackoverflow here

'''
for this particular image it is a bit challenging to add the third line from the last.
as I did some pre-processing and research for this particulr image (data/sanskrit/files/page-8.jpeg) to this image and
the best way is to crop it and then process by part.

NB: I also tried to use bounding box. I commented out the code below for that. Result files are in temp directory.
'''

import cv2
import pytesseract
import func
from func import *

image = cv2.imread("data/sanskrit/files/page-8.jpeg")
base = image.copy()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# tried another method
'''
blur_image = cv2.GaussianBlur(gray_image, (3,3), 0)
cv2.imwrite("temp/blurred_image.jpeg", blur_image)
threshold = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
cv2.imwrite("temp/thresh_image.jpeg", threshold)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 12))
cv2.imwrite("temp/kernel_image.jpeg", kernel)

dilate = cv2.dilate(threshold, kernel, iterations=1)
cv2.imwrite("temp/dilated_image.jpeg", dilate)
contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

for i in contours:
    x, y, w, h = cv2.boundingRect(i)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite("temp/bbox_image.jpeg", image)
'''

cropped_img = func.crop(gray_image, 230, 200, 1770, 1200)
# cv2.imshow("output", cropped_img) # for viewing only # close the window for further processing
# cv2.waitKey(0)

# preprocessing # adding parameters
val_1 = func.remove_noise(cropped_img, 1, 2)
val_2 = func.dilation(val_1, 1)

# for col 1
col_1 = func.crop(val_2, 10, 0, 1770, 720)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", col_1)
cv2.waitKey(0)
ocr = pytesseract.image_to_string(col_1, lang='san')

with open("output\output-page-8\output-page-8-1.txt", "w", encoding="utf-8") as text_file:
    text_file.write(ocr)

# avoiding col 2
# for col 3
col_3 = func.crop(val_2, 10, 950, 1770, 720)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", col_3)
cv2.waitKey(0)
ocr = pytesseract.image_to_string(col_3, lang='san')
with open("output\output-page-8\output-page-8-3.txt", "w", encoding="utf-8") as text_file:
    text_file.write(ocr)