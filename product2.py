# ตัวกรอง Convolution ด้วย Filter2D
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/no-3089.jpg",0)

convo1 = cv.filter2D(img,-1,np.ones((3,3),np.float32)/9)
convo2 = cv.filter2D(img,-1,np.ones((5,5),np.float32)/25)

titles = ["Original","Convolution 3x3","Convolution 5x5"]
images = [img,convo1,convo2]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()