import matplotlib.pyplot as plt
import cv2
import numpy as np
from HopefulDaugman import find_boundary

### Resizing , cropping in rgb
image = cv2.imread('L1.JPG')
M, N, C = image.shape
im_rgb_res = cv2.resize(image, (int(N/6),int(M/6)))
M2, N2, C2 = im_rgb_res.shape
im_rgb_foc = im_rgb_res[int(0.2*M2):int(0.8*M2), int(0.4*M2):int(M2)] 
cv2.imshow('Eye Focus', im_rgb_foc)


### Resizing, cropping in gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im_gray_res = cv2.resize(gray, (int(N/6),int(M/6)))
M2, N2 = im_gray_res.shape
im_gray_foc = im_gray_res[int(0.2*M2):int(0.8*M2), int(0.4*M2):int(M2)]
cv2.imshow('Eye Focus', im_gray_foc)
  
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find iris coordinates
#image2 = cv2.imread('AnotherIris.png')
image2 = cv2.imread('L1.JPG')
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


## Find iris coordinates
image2 = cv2.imread('AnotherIris.png')
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

minimal_iris_radius =30
iris_coordinates = find_boundary(gray2, minimal_iris_radius) #im_gray_foc
print(iris_coordinates)
iris_center, iris_rad = iris_coordinates
#   Drawing the circle
out = im_rgb_foc.copy()
iris_segmented = cv2.circle(image2, iris_center, iris_rad, (255, 0, 0), 2)

### finding pupil coordinates:
minimal_pupil_radius =10
coordinates = find_boundary(gray2, minimal_pupil_radius) #im_gray_foc
print(coordinates)
pupil_center, pupil_rad = coordinates
#      Drawing the circle

pupil_segmented = cv2.circle(iris_segmented, pupil_center, pupil_rad, (255, 0, 0), 2)
cv2.imshow('Segmented Iris', pupil_segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()

