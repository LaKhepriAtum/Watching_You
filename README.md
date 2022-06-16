# Watching_You (Scanning Service)

## 1. 프로젝트 개요

### 기존 박물관 애플리케이션 에서도 비컨(블루투스) 이나 <br>
### QR코드 방식으로 문화재 인식을 사용하고 있지만 정확도나 <br>
### ,거리의 제약이 있다. 그래서 추가적으로 YOLO 5 모델을 <br>
### 활용하여 기존의 방식과 다른 방식으로 프로젝트 아이템으로  <br>
### 선정하게 됨  <br>
 
2. 프로젝트 과정  <br>

데이터 수집 - 전처리 - 모델링 - 테스트 순으로 진행  <br>

A. 데이터 수집 <br>
데이터 수집 과정 중 여러 가지 시도를 시도하였지만  <br>
최종적으로 동영상 촬영 후 프레임 단위로  <br>
정제하여 MARK를 시도함 <br> 

B. 데이터 전처리 <br>
데이터 전처리 과정은 크게 두 가지로 구성되어 있음 <br>

 B-1 동영상 프레임 단위로 컷하기 <br>
https://github.com/LaKhepriAtum/Watching_You/tree/seungchae <br>
 B-2 YOLO_mark를 이용하여 라벨링 작업 <br>
https://github.com/AlexeyAB/YOLO_mark <br>

C. 모델링(학습) <br>
YOLO 5 모델 중 애플리케이션에 탑재에 가장 적합한  <br>
YOLO_5v를 활용하여 학습을 진행하게 된 정확도를 올리기 위해 <br>
batch_size 및 옵티마이저_size 등 여러 가지 <br>
조건으로 학습시킨 결과 여러 가지 조건을  <br>
실험하고 결과를 만들게 됨 <br>
https://github.com/LaKhepriAtum/Watching_You/blob/suchan/training_testing_yolov5.ipynb<br>

D. 테스트  <br>
1차 테스트는 현장에서 찍은 영상(평가세트와 불일치)으로 <br>
https://www.youtube.com/watch?v=EfYu60_XQDs <br>  
Detect.p를 활용하여 테스트하였고 <br>
2차 테스트는 국립중앙박물관 유튜브 채널에 올라와 있는  <br>
https://www.youtube.com/watch?v=JAKt8DXtf2Y <br>
영상으로 테스트 하였고 <br>
3차 테스트는 애플리케이션에 탑재하여 직접 테스트하였다 <br>
https://www.youtube.com/shorts/5XdSjF3kRac<br> 

3. 프로젝트 결과 <br>
인공지능을 배우면 배울수록 데이터의 양과 질이 중요함을 매번 느낀다 <br>
직접 현장에서 데이터 수집도 하고 테스트도 하고 라벨링 작업도 하고<br>
일련의 과정을 느낄 수 있었던 프로젝트 이였다. <br>
