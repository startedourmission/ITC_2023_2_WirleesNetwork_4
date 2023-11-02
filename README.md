# ITC_2023_2_무선네트워크_4


인하공업전문대학 2023-2학기 무선네트워크 프로젝트 4조

조원 : 박세현, 유성운, 차진우, 최민주, 최진혁, 홍승호


# Concept

### 아이디어제목 - 차진우

#### 1. 개요

초기 아이디어 회의를 위한 단락입니다.  이와 같은 양식으로 작성해주세요. 반드시 모든 항목을 채우지 않아도 되며, 아이디어가 완전하지 않아도 괜찮습니다. 필요하다면 항목을 추가/수정하여 작성해도 됩니다.  

제안된 아이디어에 대한 의견이나 피드백은 다음 이슈를 사용하세요
https://github.com/startedourmission/ITC_2023_2_WirleesNetwork_4/issues/1#issue-1969961494

#### 2. 개발 목적

아이디어가 완전히 새로울 필요는 없습니다. 다만 기획 + 필요 물품 배송 기간 +  구현 및 완성 기간을 고려하여 4~5주 내 완성될 수 있도록 스케일링해야합니다. 

#### 3. 필요 기술

1. 기반 : 라즈리파이, 아두이노
2. 센서 : 무슨무슨 센서
3. 언어 : Python

#### 4. 참조

참고한 논문, 블로그 책 등을 반드시 기록해주세요

***

### 택배 도난 방지 시스템 - 최진혁

#### 1. 개발 목적
![](https://github.com/startedourmission/ITC_2023_2_WirleesNetwork_4/blob/main/etc/%EC%B4%88%EC%95%88%20%EB%B3%B4%EA%B4%80%ED%95%A8.PNG)

CCTV가 없는 집에 경우 집앞에 놓여진 택배가 도둑 맞을 가능성이 있기에
지하철의 보관함처럼 택배 보관함을 집앞에 설계 할려고 합니다.

#### 2. 기반

1. 라즈베리파이
2. 아두이노 무게감지 센서
3. NFC 모듈
4. 도어락
5. 카메라 센서

#### 3. 사용 기술

- 도어락 제어 : 아두이노 / python , C언어
- 라즈베리파이를 통해서 사용자에 핸드폰에 보관함의 상태 변화를 전송
- (추가 예정)


#### 4. 참조
https://twinw.tistory.com/136

***

### AI 선풍기 - 차진우


![](etc/sample1.png)

#### 1. 개발목적

기존 선풍기는 고정된 각도로 회전하도록 되어있기 때문에 비효율이 발생. 선풍기가 사람 없는 쪽으로 바람을 보내는 시간동안 더워하는 것이 고통스러움. 또한 선풍기가 멀리 있을 경우 각도를 조절하거나 가까이 가져오기 번거로움.

#### 2. 필요 장비 및 센서

1. 아두이노, 라즈베리파이
2. pi카메라
3. 선풍기 회전 및 바퀴에 사용될 모터
4. 선풍기 날개

#### 3. 사용 기술

- 선풍기 조작 : 아두이노 / Python
- 라즈베리파이 -> 서버 영상 전송 : 스트리밍 (g streamer, ffmpeg 등) 고려 중
- 서버 -> 라즈베리파이 데이터 전송 : 웹 소켓 고려 중
- 딥러닝 영상 처리 -> Pre-trained Object Detection 모델 (YOLO 등)
