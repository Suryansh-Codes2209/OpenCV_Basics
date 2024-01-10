# capturing image in live stream ()

import cv2

cap = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.mp4' , fourcc , 50.0 , (640,480))

while (True):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_BITRATE))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_AUTO_EXPOSURE))

        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
