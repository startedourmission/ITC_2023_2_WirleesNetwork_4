
## http 통신

```python
import requests

def httpcliet():
	url = ''
	files = {'file': open('', 'rb')}
	
	response = requests.post(url, files=files) # SSL 인증을 위해 필요한 경우
	print(response.text)

httpcliet()


```

```
import requests
from picamera2 import PiCamera2
from time import sleep

# HTTP 서버 주소
SERVER_URL = 'http://your_server_address/upload'  # 실제 서버 주소 입력

# 카메라 초기화
camera = PiCamera2()

# 이미지 전송 함수
def send_picture(picture):
    picture.seek(0)	# 파일 포인터를 처음으로 옮김
    files = {'image': ('image.jpg', picture.getvalue())}
    try:	# http 응답 성공 : 200, Not found : 404, Forbidden : 403, Internal Server Error : 500
        response = requests.post(SERVER_URL, files=files)
        if response.status_code == 200:
            print("이미지 전송 성공")
        else:
            print("이미지 전송 실패:", response.status_code)
    except requests.RequestException as e:
        print("요청 실패:", e)

# 한 프레임씩 이미지 캡처 및 전송
try:
    while True:
        picture = '/tmp/frame.jpg'  # 임시 파일로 저장
        camera.capture(picture)
        with open(frame, 'rb') as f:
            send_picture(f)
        sleep(1)  # 1초 간격으로 전송
finally:
    camera.close()
```
# 사람인식-> 사람이 감지될 때만 사진

https://blog.naver.com/ljy9378/221438230814
```
