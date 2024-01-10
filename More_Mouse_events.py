import cv2 
import numpy as np

def click_M(event , x,y , flags , param):
    
    print(x , " , " , y )
    font = cv2.FONT_HERSHEY_COMPLEX
    xyvalue = str(x) + " , " + str(y)
    cv2.putText()