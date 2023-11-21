import base64
import time
import websocket
from picamera import PiCamera
from io import BytesIO

def send_frame(ws, frame):
    # 영상 프레임을 base64 인코딩 문자열로 변환
    encoded_string = base64.b64encode(frame.getvalue()).decode('utf-8')
    # 웹소켓을 통해 인코딩된 문자열 전송
    ws.send(encoded_string)

# 웹소켓 연결 초기화
ws = websocket.WebSocket()
ws.connect("ws://your_server_ip:5000")

camera = PiCamera()

# 카메라 설정
camera.resolution = (640, 480)
camera.framerate = 24

# 영상 스트림을 시작
with BytesIO() as frame:
    for _ in camera.capture_continuous(frame, 'jpeg', use_video_port=True):
        frame.seek(0)
        send_frame(ws, frame)
        frame.truncate()
        time.sleep(0.04)  # 대략 24 fps에 해당하는 지연