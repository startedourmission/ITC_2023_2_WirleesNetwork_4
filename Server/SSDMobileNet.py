import numpy as np
import cv2

# 모델 경로 설정
prototxt_path = 'model/MobileNetSSD_deploy.prototxt.txt'
model_path = 'model/MobileNetSSD_deploy.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

def detect_objects(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    vis = image.copy()
    results = []
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:
            idx = int(detections[0, 0, i, 1])
            if CLASSES[idx] == "person":
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                centerX = int((startX + endX) / 2)
                centerY = int((startY + endY) / 2)
                results.append({
                    "class": CLASSES[idx],
                    "confidence": float(confidence),
                    "box": [int(startX), int(startY), int(endX), int(endY)],
                    "center": [centerX, centerY]
                })
                cv2.rectangle(vis, (startX, startY), (endX, endY), (255, 0, 0), 2)  # 빨간색 박스로 표시
                cv2.circle(vis, (centerX, centerY), 4, (0, 255, 0), -1)  # 중앙에 초록색 점 표시

    # # OpenCV window로 이미지 표시
    # max_height = 1000
    # height, width = vis.shape[:2]
    # if height > max_height:
    #     ratio = max_height / height
    #     vis = cv2.resize(vis, (int(width * ratio), max_height))
    # cv2.imshow('Detected Objects', vis)
    # cv2.waitKey(0)  # 사용자가 키를 누를 때까지 대기
    # cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기
    return results
