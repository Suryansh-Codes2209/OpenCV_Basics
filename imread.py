#reading image in OpenCV 

import cv2

a = cv2.imread("data\prism_blackbg.jpg",1)
print(a)

cv2.imshow('Preview',a)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('data\image1.jpg' , a)
