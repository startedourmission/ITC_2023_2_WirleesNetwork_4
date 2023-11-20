# app.py
import io
from PIL import Image
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from SSDMobileNet import detect_objects
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@socketio.on('message')
def handle_message(message):
    now = datetime.now().strftime("%Y%m%d_%H:%M:%S")
    client_ip = request.remote_addr
    print('received message: ' + message)
    image_stream = io.BytesIO(message)
    image = Image.open(image_stream)
    image.save(str(client_ip) + now +'.jpg')

@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        now = datetime.now().strftime("%Y%m%d_%H:%M:%S")
        client_ip = request.remote_addr
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, str(client_ip) + "_" + now + '_' + filename)
        file.save(file_path)

        # 이미지 객체 탐지
        results = detect_objects(file_path)
        # 임시 이미지 삭제
        #os.remove(file_path)
        return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
