import cv2 

img = cv2.imread('data\prism_blackbg.jpg' , 0)

img = cv2.line(img, (0,0) , (255,255) , (255,255,255) , 15)
img = cv2.arrowedLine(img, (255,255) , (800,600) , (255,255,255) , 15)

img = cv2.rectangle(img, (400,200), (510,120),(255,255,255),5)
img = cv2.circle(img, (400,200), 45,(255,255,255),2)



cv2.imshow("Line Preview" , img)

cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()