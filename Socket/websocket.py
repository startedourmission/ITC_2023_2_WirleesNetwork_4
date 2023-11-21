import websocket
import _thread
import time
import base64

def send_image(ws):
    file_path = 'path/to/your/image.jpg'  # 이미지 파일 경로
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    ws.send(encoded_string)

def on_message(ws, message):
    print("Received message from server: " + message)

def on_error(ws, error):
    print("Error: " + str(error))

def on_close(ws):
    print("### Connection closed ###")

def on_open(ws):
    _thread.start_new_thread(send_image, (ws,))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://yourserver.com:port",
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()