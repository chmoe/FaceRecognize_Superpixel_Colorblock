# -*- coding: UTF-8 -*-
# @Project: Face_recognition 
# @File: MTCNN 
# @Author: Henry Wu 
# @Date: 2021/09/25 14:36

import cv2
from mtcnn import MTCNN  # conda install mtcnn
import copy

# detector
detector = MTCNN()

for i in range(37):

    img = cv2.imread(r'./picture/' + str(i) + '.jpg')
    img = cv2.resize(img, dsize=(480, 640))

    face_frame = copy.deepcopy(img)

    # BGR2RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 检测出人脸的四个点
    dets = detector.detect_faces(img_rgb)

    for face in dets:
        # 座標と高幅を取得
        box_x, box_y, box_w, box_h = face['box']
        # 顔のトリミング
        face_image = face_frame[box_y:box_y + box_h, box_x:box_x + box_w]

        # 顔箇所にMTCNN文字を表示
        cv2.putText(face_frame, "MTCNN", (box_x, box_y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        # 顔箇所を四角で描画
        cv2.rectangle(face_frame, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 255, 0), 2)

        for key, value in face['keypoints'].items():
            # 顔のランドマーク箇所に小さい赤色サークルを描画（目、鼻、口）
            cv2.circle(face_frame, value, 1, (0, 0, 255), -1)
        # 顔だけをファイルに保存
        cv2.imwrite('./result/MTCNN/' + str(i) + '.png', face_frame)
