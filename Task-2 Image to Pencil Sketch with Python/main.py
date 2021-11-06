'''
    LGMVIP Data Science Internship
    Task2- Image to Pencil Sketch with Python
    Author : Taabish Farid Khan
'''

# Importing Libraries
import cv2

# Getting image location and filename
location = '/home/taabish/Documents/LGMVIP/Task2-Image to Pencil Sketch with Python/'
filename = 'cat.jpg'


# CREATING IMAGES


# Reading the original image
image = cv2.imread(location + filename)

# Reading the black and white image
bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inverting the image
inverted_image = 255 - bw_image

# Blurring the image
blurred_image = cv2.GaussianBlur(inverted_image, (21,21), 0)

# Inverting the blurred image
inverted_blurred_image = 255 - blurred_image

# Creating the Pencil Sketch image
pencil_sketch_image = cv2.divide(bw_image, inverted_blurred_image, scale=256.0)


# DISPLAYING IMAGES


# Displaying the Original Image
cv2.imshow('Original Image', image)

# Displaying the Black and White Image
cv2.imshow('B&W Image', bw_image)

# Displaying the Inverted Image
cv2.imshow('Inverted Image', inverted_image)

# Displaying the Blurred Image
cv2.imshow('Blurred Image', blurred_image)

# Displaying the Inverted Blurred Image
cv2.imshow('Inverted Blurred Image', inverted_blurred_image)

# Displaying the Pencil Sketch Image
cv2.imshow('Pencil Sketch Image', pencil_sketch_image)


cv2.waitKey(0)