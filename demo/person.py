from ultralytics import YOLO

# 変更
movie_path = './data/test.mp4'
#

model_path = './model/person/yolov8m-pose.pt'
model = YOLO(model_path)
results = model(movie_path, save=True, show=True)