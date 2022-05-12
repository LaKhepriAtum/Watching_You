import cv2
import os

videoPath = './datasets/video/'
imagePath = 'C:\\Watching_You\\images\\'

file_list = os.listdir(videoPath)
print(file_list)
for file in file_list:
    print(file)
    vidcap = cv2.VideoCapture(videoPath+file)
    print(vidcap)
    file = file[:-4]
    success,image = vidcap.read()
    count = 0

    print(success)
    print(image)
    while success:
        cv2.imwrite(imagePath + file +"." +"%0d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        if (int(vidcap.get(1)) % 10 == 0):  #프레임 별로 자르기
            print('Read a new frame: ', success)
            count += 1

data_path = 'C:\\Watching_You\\images'
train_data_path = data_path + '\\train'
for root, dirs, files in os.walk(data_path):
    for file in files:
        str_class_name = file.split('.')[0]
        print(str_class_name)
        des_path = data_path + '\\train' + '\\' + str_class_name
        if not os.path.exists(des_path):
            os.makedirs(des_path)
        os.rename(data_path + '\\' + file, des_path + '\\' + file)

