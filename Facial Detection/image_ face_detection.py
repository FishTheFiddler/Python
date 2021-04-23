#######################################################
# Program: face_detection2.py                         #
# Prerequitsites: Must install "numpy" and            #
#                 "opencv-python" via pip.            #
# Author: Fish the Fiddler                            #
# Date: 2/1/2021                                      #
# Purpose: The goal is to take an existing            #
#          compatible image and detect any faces.     #
# Input: Compatible Image file                        #
# Output: Image file with rectangle around the face.  #
#######################################################

# Import library modules
import cv2
import os.path
from os import path


while True:
    # Opening prompt for user
    image = input("\nWelcome to the Facial Detection program! \nTo begin, please type in the name and extension of your image. (i.e. \"shepard.jpg\") \n \nImage: ")

    # Check for a valid file using the user's input. If the file is valid, continue through process. Otherwise, reject input and offer to try again.
    if path.isfile(image):
        print ("Thank you, processing file...")
        
    # Load the cascade file provided by intel source. (This .XML file is located in
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
        img = cv2.imread(image)

    # Convert image into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw Rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
        cv2.imshow('img', img)
        cv2.waitKey(1)

    else:
    # Reject input and Offer to try again by pressing any key.  Also offer to quit progrma by typing "n"
        print ("\nI'm sorry. The file name you provided is unrecognized. Please try the following: \n-Use the file name and extension. (i.e. \"shepard.jpg\")\n-Ensure the file is in the correct directory.")
    try_again = input("Press any key to try again, or type \"n\" to quit: ")
    if try_again.lower() == "n":
        break
        exit()
    
