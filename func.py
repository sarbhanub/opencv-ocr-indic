# author: sbaidya
# date: 08.04.2021
# most of the functions that i am going to use

import cv2

# function to crop my image
def crop(image, y, x, h, w):
    cropped_image = image[y:y + h, x:x + w]
    return cropped_image

# thickens the font# second parameter for the level
def dilation(image, iteration):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=iteration)
    image = cv2.bitwise_not(image)
    return image

# thinness the font # second parameter for the level
def erosion(image, iteration):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations=iteration)
    image = cv2.bitwise_not(image)
    return image


# removes noise # using morphology
# value = effect of smoothing # weight = adds blur
def remove_noise(image, value, weight):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=value)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=value)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.GaussianBlur(image, (7,7), 2) # adding gaussian blur helped a lot compared to median blur
    return image