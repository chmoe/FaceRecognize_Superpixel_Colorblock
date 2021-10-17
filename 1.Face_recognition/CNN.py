# -*- coding: UTF-8 -*-
# @Project: Face_recognition 
# @File: CNN 
# @Author: Henry Wu 
# @Date: 2021/09/25 14:07

import dlib
import cv2
import copy

# CNN
cnn_fn = './mmod_human_face_detector.dat'
cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_fn)

for i in range(37):

    img = cv2.imread(r'./picture/' + str(i) + '.jpg')
    img = cv2.resize(img, dsize=(480, 640))

    face_frame = copy.deepcopy(img)

    # 检测出人脸的四个点（起始坐标x,y xy方向的长度）
    dets = cnn_face_detector(img, 1)

    for face in dets:
        # 顔のトリミング
        face_image = face_frame[face.rect.top():face.rect.bottom(), face.rect.left():face.rect.right()]

        cv2.putText(img, "CNN", (int(face.rect.left()), int(face.rect.top()) - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 1, cv2.LINE_AA)
        # 顔箇所を四角で描画
        cv2.rectangle(img, (face.rect.left(), face.rect.top()), (face.rect.right(), face.rect.bottom()), (0, 255, 0),
                      2)
        # 顔だけをファイルに保存
        cv2.imwrite('./result/CNN/' + str(i) + '.png', img)
