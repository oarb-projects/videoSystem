from flask import Flask, render_template, Response, jsonify, request
from camera import VideoCamera
import cv2
import time

app = Flask(__name__)

video_camera = None
global_frame = None
# https://www.whatismybrowser.com/detect/what-is-my-ip-address
# 201.143.139.170
# netstat -na|findstr 8080
def obten_video():
    # fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')  
    fourcc = cv2.VideoWriter_fourcc(*'X264')
    out = cv2.VideoWriter('output.avi',fourcc, 26.92, (640,480))
    #this will show all available
    # out = cv2.VideoWriter('output.avi',-1, 20.0, (640,480))
    # print(returnCameras())
    
    # cap =cv2.VideoCapture(1)

    # Number of frames to capture
    url='http://127.0.0.1:7777/axis-cgi/mjpg/video.cgi?cameraId=547769470&user=admin&pwd=1234'
    cap=cv2.VideoCapture(url)


    num_frames = 120
     
     
    print("Capturing {0} frames".format(num_frames))

    # Start time
    start = time.time()
     
    # Grab a few frames
    for i in range(0, num_frames) :
        ret, frame = cap.read()
 
     
    # End time
    end = time.time()
 
    # Time elapsed
    seconds = end - start

    print("Time taken : {0} seconds".format(seconds))
    # Calculate frames per second
    fps  = num_frames / seconds
    print("Estimated frames per second : {0}".format(fps))
    while(cap.isOpened()):
        #width = cap.get(3)   # float
        #height = cap.get(4) # float
        #print("width {} height {}".format(width,height))
        ret, frame = cap.read()
        if ret==True:
            # write the flipped frame
            # frame = cv2.flip(frame,0)

            out.write(frame)
            cv2.imshow('frame',frame)
    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def video_stream():
    global video_camera 
    global global_frame

    if video_camera == None:
        video_camera = VideoCamera()
        
    while True:
        frame = video_camera.get_frame()

        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')

#list all availablecameras
def returnCameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/camara")
def camara():
    return render_template('index.html')

@app.route("/obten")
def obten():
    obten_video()
    return "video obtenido"

@app.route('/record_status', methods=['POST'])
def record_status():
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        video_camera.start_record()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        return jsonify(result="stopped")

@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')  

if __name__ == "__main__":
 app.run(debug=True,host='0.0.0.0', port=8080)


