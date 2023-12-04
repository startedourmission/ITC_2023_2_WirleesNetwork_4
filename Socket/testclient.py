import requests
import subprocess
import time
import json
import serial

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600)
except:
    pass

def httpclient(frame):
    response = requests.post('http://165.246.38.171:5000/upload', files=frame)
    data = response.text
    return data

id = 0
while True:
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600)
        subprocess.run("fswebcam -r 180*180 --no-banner " + '/home/admin/201944100/' + str(id) + '.jpg', shell=True)
        files = {'file' : open('/home/admin/201944100/' + str(id) + '.jpg', 'rb')}
    
        obj = json.loads(httpclient(frame = files))
        for i in obj:
            print('y:', i['center'][0])
            test1 = int(i['center'][0])          
            str1 =  ("Scontrol:" + str(test1))
            ser.write(bytes(str1.encode()))

            print()
            time.sleep(3) 

    except Exception as e:
        print(e)

ser.close()
