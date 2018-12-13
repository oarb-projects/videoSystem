import cv2
url='http://127.0.0.1:7777/axis-cgi/mjpg/video.cgi?cameraId=547769470&user=admin&pwd=1234'

# url='http://192.168.1.64:7777/axis-cgi/mjpg/video.cgi?cameraId=924419706&user=admin&pwd=1234'
# http://192.168.1.68:7777/axis-cgi/mjpg/video.cgi?cameraId=924419706&user=admin&pwd=1234
cap=cv2.VideoCapture(url)

# import cv2
# capture = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1')
# capture = cv2.VideoCapture('rtsp://192.168.1.64/1')



while(cap.isOpened()):
    #width = cap.get(3)   # float
    #height = cap.get(4) # float
    #print("width {} height {}".format(width,height))
    ret, frame = cap.read()
    if ret==True:
        # write the flipped frame
        # frame = cv2.flip(frame,0)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()