import requests
import subprocess
import time
import json
import serial

try:
     # 시리얼 포트 초기화
    ser = serial.Serial('/dev/ttyAMA0', 9600)
except:
    pass

def httpclient(frame):
    response = requests.post('http://165.246.38.171:5000/upload', files=frame)
    data = response.text
    return data

id = 0
while True:
    try:
         # 시리얼 포트 다시 초기화
        ser = serial.Serial('/dev/ttyAMA0', 9600)

        # fswebcam을 사용하여 이미지 캡처
        subprocess.run("fswebcam -r 180*180 --no-banner " + '/home/admin/201944100/' + str(id) + '.jpg', shell=True)

         # 업로드를 위해 파일 준비
        files = {'file' : open('/home/admin/201944100/' + str(id) + '.jpg', 'rb')}

        # 이미지 데이터를 서버에 보내고 응답을 받음
        obj = json.loads(httpclient(frame = files))

        # 받은 데이터를 처리하고 시리얼 디바이스에 명령을 보냄
        for i in obj:
            print('y:', i['center'][1])
            ser.write(str.encode("Scontrol:"+str(i['center'][1])))  
            print()
            time.sleep(3) 

    except Exception as e:
        print(e)

ser.close()
