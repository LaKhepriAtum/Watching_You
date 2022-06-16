# Watching_You (Scanning Service)

### 1. 프로젝트 개요

#### 기존 박물관 애플리케이션 에서도 비컨(블루투스) 이나 
#### QR코드 방식으로 문화재 인식을 사용하고 있지만 정확도나 
#### ,거리의 제약이 있다. 그래서 추가적으로 YOLO 5 모델을 
#### 활용하여 기존의 방식과 다른 방식으로 프로젝트 아이템으로  
#### 선정하게 됨  
<br>
<br>
 
### 2. 프로젝트 과정 

#### 데이터 수집 - 전처리 - 학습 - 테스트 순으로 진행  

<br>
<br>


### 데이터 수집 
###### 데이터 수집 과정 중 여러 가지 시도를 시도하였지만  
###### 최종적으로 동영상 촬영 후 프레임 단위로  
######  정제하여 MARK를 시도함 <br> 
###### ![image](https://user-images.githubusercontent.com/96555334/174024303-50217827-4235-4e31-8bc8-70bb5080734a.png)

<br>
<br>

### 데이터 전처리 
#####  동영상 > 이미지 분할  
##### ![image](https://user-images.githubusercontent.com/96555334/174024843-c0964308-1fdc-439c-8d83-82a089bc5e32.png)
##### job01 frame_cut.py  (seungchae-branch)

<br>
<br>

### 이미지 라벨링(Yolo_mark)
##### ![image](https://user-images.githubusercontent.com/96555334/174025322-12fdf7e6-dbde-4aae-9968-3f8927b1d2c4.png)
##### https://github.com/AlexeyAB/Yolo_mark
<br>
<br>

### 학습
#### ![image](https://user-images.githubusercontent.com/96555334/174025693-8a55e64b-2e38-4be1-b65c-0cd347534dcf.png)
#### job01 yolo5v.ipynb  (suchan-branch)

<br>
<br>

### Test
#### ![image](https://user-images.githubusercontent.com/96555334/174026991-5595a0dd-8ab6-4651-8ff1-85c9f028fd35.png)
#### ![image](https://user-images.githubusercontent.com/96555334/174027015-e871f84b-d7c1-4eb8-aee4-fa174f0862ce.png)

<br>
<br>

###  결과
<br>

#### 1차 현장 영상(테스트)
https://www.youtube.com/watch?v=EfYu60_XQDs 

#### 2차 국립중앙박물관(유튜브) 
https://www.youtube.com/watch?v=JAKt8DXtf2Y

#### 3차 애플리케이션 테스트 
https://www.youtube.com/shorts/5XdSjF3kRac<br> 


