from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-f","--face", required=True,
    help="path to where the face cascade resides")
ap.add_argument("-i","--image", required=True,
    help="path to where the image file resides")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)