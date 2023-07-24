import sys
from PIL import Image,ImageEnhance
import matplotlib.pyplot as plt
import numpy as np

im1 = Image.open("C:\Users\Ishika\Desktop\bits pilani\Team Anant\payload\calibration\testimage1.jpeg")
im1 = im1.convert('LA') #Converts to grayscale
im2 = im1
width,height = im1.size

#Both the images are same. To calibrate we need to change intensity of radiance.

enhancer = ImageEnhance.Brightness(im2)
factor = 0.8
#80% of original intensity
im2 = enhancer.enhance(factor)

#Check the images visually
im1.show()
im2.show()

#grayscale histograms
hist,bin = np.histogram(im1.histogram())

plt.plot(hist)
plt.title('histogram')

plt.show()

hist,bin = np.histogram(im2.histogram())

plt.plot(hist)
plt.title('histogram')

plt.show()

total = 0
pixels = width*height

for i in range(0,width):
    for j in range(0,height):
        total += im1.getpixel((i,j))[0]

MeanDN1 = total/pixels
total = 0

for i in range(0,width):
    for j in range(0,height):
        total += im2.getpixel((i,j))[0]

MeanDN2 = total/pixels

print(MeanDN1)
print(MeanDN2)

radiance1 = 100
radiance2 = radiance1*0.8
gain = (MeanDN1-MeanDN2)/(radiance1-radiance2)
bias = MeanDN1 - (gain*radiance1)

print(gain)
print(bias)