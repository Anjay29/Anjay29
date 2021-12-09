
import cv2
import numpy as np
# import matplotlib.pyplot as plt
img= cv2.imread('red4.jpg',1)
rec = cv2.imread('red4.jpg',1)
rec   = cv2.inRange(rec, (100,0,0) , (225,80,80))
cv2.imshow('image',img)
print(img.shape)
x_max=0
x_min=700
y_min=700
y_max=0
rectangle = np.where(rec > np.mean(rec), 255, 0).astype(np.uint8)    
dst_rectangle = cv2.cornerHarris(rectangle, 2, 3, 0.04)
dst_rectangle = cv2.dilate(dst_rectangle, None)
mask = np.where(dst_rectangle > 0.01*np.max(dst_rectangle), 255, 0).astype(np.uint8)
points = np.nonzero(mask)
a=len(points[0])
b=len(points[1])
m=0
n=0
while m<a:
    x=points[0][m]
    y=points[1][m]
    if x>x_max:
        x_max=x
    if x<x_min:
        x_min=x
    m=m+1
while n<b:
    x=points[0][n]
    y=points[1][n]
    if y>y_max:
        y_max=y
    if y<y_min:
        y_min=y
    n=n+1
c1x=int((x_min+x_max)/2)
c2x=int((x_min+x_max)/2)
c3x=int((x_min+x_max)/2)
c1y=int(y_min+(-y_min+y_max)*0.25)
c2y=int(y_min+(-y_min+y_max)*0.5)
c3y=int(y_min+(-y_min+y_max)*0.75)

red_light=False
green_light=False
yellow_light=False
if img[c1y,c1x,0]<20 and img[c1y,c1x,1]>200 and img[c1y,c1x,2]<20:
    green_light=True
elif(img[c1y,c1x,0]<127 and img[c1y,c1x,1]>128 and img[c1y,c1x,1]<=255 and img[c1y,c1x,2]>128 and img[c1y,c1x,2]<=255): 
    yellow_light=True
elif(img[c1y,c1x,0]<20 and img[c1y,c1x,1]<20 and img[c1y,c1x,2]>200):
    red_light=True
    
    
if img[c2y,c2x,0]<20 and img[c2y,c2x,1]>200 and img[c2y,c2x,2]<20:
    green_light=True
elif(img[c2y,c2x,0]<127 and img[c2y,c2x,1]>128 and img[c2y,c2x,1]<=255 and img[c2y,c2x,2]>128 and img[c2y,c2x,2]<=255): 
    yellow_light=True
elif(img[c2y,c2x,0]<20 and img[c2y,c2x,1]<20 and img[c2y,c2x,2]>200):
    red_light=True
    
    
if img[c3y,c3x,0]<20 and img[c3y,c3x,1]>200 and img[c3y,c3x,2]<20:
    green_light=True
elif(img[c3y,c3x,0]<127 and img[c3y,c3x,1]>128 and img[c3y,c3x,1]<=255 and img[c3y,c3x,2]>128 and img[c3y,c3x,2]<=255): 
    yellow_light=True
elif(img[c3y,c3x,0]<20 and img[c3y,c3x,1]<20 and img[c3y,c3x,2]>200):
    red_light=True
    
if red_light==True and yellow_light==False and green_light==False:
    print("The light is red")
elif yellow_light==True and red_light==False and green_light==False:
    print("The light is yellow")
elif green_light==True and red_light==False and yellow_light==False:
    print("The light is green")
else:
    print("Error")
cv2.waitKey(0)
cv2.destroyAllWindows()