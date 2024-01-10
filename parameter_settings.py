import cv2 

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3,9000)
cap.set(4,4000)

print(cap.get(3))
print(cap.get(4))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Video_Frames',frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()
