C:\Users\oscar\Desktop\Constructora\Scripts\activate.bat
https://github.com/cisco/openh264/releases/tag/v1.6.0
se puso en carpeta raiz de app

https://community.logitech.com/s/question/0D53100006aQKidCAG/what-is-the-frame-rate-of-the-c920
http://answers.opencv.org/question/135646/videowriter-fps-parameter/
https://www.learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/
https://docs.opencv.org/3.0-beta/modules/videoio/doc/reading_and_writing_video.html?highlight=videowriter
http://flask.pocoo.org/docs/1.0/quickstart/

wyze cam v2
model wyzec2
fcc id: 2anjhwyezc2
mac: 2C:AA:8E:01:6A:58
arp -a
arp -a 192.168.1.81

http://192.168.1.68:8083/live?tag=*
http://192.168.1.68:8083/axis-cgi/mjpg/video.cgi?cameraId=924419706
copy image address
https://www.ispyconnect.com/sources.aspx
https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
http://192.168.1.81:8090/video
https://reolink.com/rtsp-ip-camera-and-best-rtsp-camera-buying-guide/
https://tinycammonitor.com/manual/app_web_server.html
http://192.168.1.68:8083/static/api.html
https://ipcamtalk.com/threads/looking-for-free-cloud-storage.10638/
https://www.raspberrypi-spy.co.uk/2017/04/raspberry-pi-cctv-camera-with-motioneyeos/
https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv

https://xael.org/norman/python/python-nmap/
https://www.programcreek.com/python/example/92225/nmap.PortScanner
ON CMD 
where nmap
after activating virtual env
pip install python-nmap


{'tcp': {'method': 'syn', 'services': '0-65535'}}
host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe
192.168.1.81;;;tcp;80;http;open;Boa HTTPd;;syn-ack;0.94.13;10;cpe:/a:boa:boa:0.94.13
192.168.1.81;;;tcp;10002;documentum;open;;;syn-ack;;3;
192.168.1.81;;;tcp;22306;;open;;;syn-ack;;;
192.168.1.81;;;tcp;22345;;open;;;syn-ack;;;

['192.168.1.81']
up
['tcp']
dict_keys([80, 10002, 22306, 22345])
True

192.168.1.81:10002/video
192.168.1.81:22306/video
192.168.1.81:22345/video
rtsp://192.168.1.81:10002/
rtsp://192.168.1.81:22306/video
rtsp://192.168.1.81:22345/video

https://www.reddit.com/r/wyzecam/comments/80o52p/q_https_mjpeg_streaming/

http://192.168.1.68:7777/axis-cgi/mjpg/video.cgi?cameraId=924419706&user=admin&pwd=1234

https://github.com/openipcamera/openipc-firmware/issues/110
https://github.com/EliasKotlyar/Xiaomi-Dafang-Hacks/issues/669
https://github.com/nblavoie/wyzecam-api
https://ipcamtalk.com/threads/is-there-a-windows-software-that-works-like-tiny-cam-pro.25298/


https://www.reddit.com/r/wyzecam/comments/9oyyyb/streaming_wyzecam_to_youtube_live/
https://www.ispyconnect.com/sources.aspx?letter=W
https://www.ispyconnect.com/man.aspx?n=Zmodo

https://www.amazon.com/slp/ip-cameras/efy8v75y65wg88n
https://gizmodo.com/a-creepy-website-is-streaming-from-73-000-private-secur-1655653510
https://www.reddit.com/r/wyzecam/comments/7w4kx4/openipc_open_source_firmware_with_rtsp_for/
https://openip.cam/#pricing
https://www.amazon.com/Zmodo-Wireless-Security-Outdoor-Recording/dp/B01IT8LO1I/ref=olp_product_details?_encoding=UTF8&me=

pip freeze
https://packaging.python.org/tutorials/managing-dependencies/#installing-pipenv
https://pipenv.readthedocs.io/en/latest/
https://docs.python.org/3/tutorial/venv.html

netstat /a

<!-- how to upload to repo -->
git init
git status
python -m pip freeze > requirements.txt
git add -A