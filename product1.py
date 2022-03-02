# Mophological
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("images/no-3089.jpg")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img_gray = cv.imread("images/no-3089.jpg",0)
thresh , result = cv.threshold(img_gray,200,255,cv.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)
# Dialation ขยายภาพ
dilation = cv.dilate(result,kernel,iterations=2)

# Erode กร่อนภาพ
erosion = cv.erode(result,kernel,iterations=2)

# Opening
openning = cv.morphologyEx(result,cv.MORPH_OPEN,kernel,iterations=2)

# Closing
clossing = cv.morphologyEx(result,cv.MORPH_CLOSE,kernel,iterations=5)

titles = ["Original","Gray","Thresh","Dilation","Erosion","Opening","Clossing"]
images = [img,img_gray,result,dilation,erosion,openning,clossing]

for i in range(len(images)):
    plt.subplot(4,3,i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()