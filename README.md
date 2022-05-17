# Watching_You

동영상 실행코드
python .\detect.py --source runs/move_mp4/bindewlq.mp4 --weight .\runs\train\Mask_wearinf_results\weights\best.pt

웹캠 실행코드
python .\detect.py --weight .\runs\train\Mask_wearinf_results\weights\mu.pt --img 410 --conf 0.5 --source 0 

모델 저장코드 (코랩버전)
!python train.py --img 416 --batch 16 --epochs 50 --data /content/drive/MyDrive/dataset/data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name gun_yolov5s_result

모델 저장코드(파이참)
python train.py --img 416 --batch 2 --epochs 50 --data C:\work\python\yolov5\data\project_datasets\dataset\data.yaml --cfg ./models/yolov5s.yaml --weights yolov5s.pt --name project_result


깃허브
https://github.com/kanghorim?tab=repositories
