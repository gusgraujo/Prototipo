import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
from functools import partial
from PIL import Image, ImageTk
import FunOpenCv

path = r"C:\_SourceCode\Prototipo\Samples\lena.jpg"


class Iris :

    def __init__(self , caminho , caminho2 ):
        self.caminho = caminho 
        self.caminho2 = caminho2


    def recCircle(caminho):
        # Read image. 
        img = cv2.imread(path, cv2.IMREAD_COLOR) 
  
        # Convert to grayscale. 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
            # Blur using 3 * 3 kernel. 
        gray_blurred = cv2.blur(gray, (3, 3)) 
  
        # Apply Hough transform on the blurred image. 
        detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 60, 
               param2 = 20, minRadius = 0, maxRadius = 0) 
  
         # Draw circles that are detected. 
        if detected_circles is not None: 
  
            # Convert the circle parameters a, b and r to integers. 
            detected_circles = np.uint16(np.around(detected_circles)) 
  
            for pt in detected_circles[0, :]: 
               a, b, r = pt[0], pt[1], pt[2] 
  
               # Draw the circumference of the circle. 
               cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
               # Draw a small circle (of radius 1) to show the center. 
               cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
               cv2.imshow("Detected Circle", img) 
               cv2.waitKey(0) 


    def build_filters():
        filters = []
        ksize = 31
        for theta in np.arange(0, np.pi, np.pi / 16):
        kern = cv2.getGaborKernel((ksize, ksize), 4.0, theta, 10.0, 0.5, 0, ktype=cv2.CV_32F)
        kern /= 1.5*kern.sum()
        filters.append(kern)
        return filters
 
    def process(img, filters):
        accum = np.zeros_like(path)
        for kern in filters:
            fimg = cv2.filter2D(path, cv2.CV_8UC3, kern)
            np.maximum(accum, fimg, accum)
        return accum


    def gabor():
        print __doc__
         try:
        img_fn = path
        except:
        img_fn = 'test.png'
 
        img = cv2.imread(img_fn)
        if img is None:
        print 'Failed to load image file:', img_fn
        
 
        filters = build_filters()
 
        res1 = process(path, filters)
        cv2.imshow('result', res1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()