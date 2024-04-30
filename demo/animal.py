from ultralytics import YOLO
import cv2

import sys
sys.path.append('utils')
from draw import *

# 変更
movie_path = './data/test.mp4'
save_path = './demo/results/results.mp4'
model_path = './model/animal/best.pt'
#

draw = Draw()
model = YOLO(model_path)
cap = cv2.VideoCapture(movie_path)
# 元の動画のサイズを取得
width = int(cap.get(3))
height = int(cap.get(4))
fps = cap.get(5)

# 動画保存の設定
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 動画のコーデックを指定
out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))  # ファイル名、コーデック、フレームレート、サイズを指定

while cap.isOpened():
    # フレームを1枚ずつ読み込む
    ret, frame = cap.read()
    if not ret:
        break
    # print(frame)
    results = model(frame, conf=0.01)
    # print(results)
    if len(results[0].boxes.xyxy) >= 1:
        for result in results:
            # print(result)
            bbox = result.boxes.xyxy[0].cpu().numpy().tolist()
            keypoints = result.keypoints.xy[0].cpu().numpy().tolist()
            # print(bbox)
            # print('='*50)
            # print(keypoints)
            keypoints, keypoints_num = keypoints_reshape(keypoints)
            frame = draw.draw_keypoints(frame, keypoints)
            frame = draw.draw_skeleton(frame, keypoints)
            frame = draw.draw_bbox(frame, bbox)
        # break

    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# キャプチャを解放
cap.release()
out.release()
# ウィンドウを閉じる
cv2.destroyAllWindows()