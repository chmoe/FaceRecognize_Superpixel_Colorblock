# -*- coding: UTF-8 -*-
# @Project: Face_recognition 
# @File: Dlib_HOG_CSM 
# @Author: Henry Wu 
# @Date: 2021/09/25 13:40

import cv2  # conda install opencv
import dlib  # github下载源码编译
import copy

print(dlib.__file__)

# Dlib
detector = dlib.get_frontal_face_detector()

for i in range(37):

    img = cv2.imread(r'./picture/' + str(i) + '.jpg')
    img = cv2.resize(img, dsize=(480, 640))

    face_frame = copy.deepcopy(img)

    # 检测出人脸的四个点（起始坐标x,y xy方向的长度）
    dets = detector(img, 1)

    for k, d in enumerate(dets):
        # 顔のトリミング
        face_image = face_frame[d.top():d.bottom(), d.left():d.right()]

        # Dlib名を書き込み
        cv2.putText(img, "Dlib", (int(d.left()), int(d.top()) - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1,
                    cv2.LINE_AA)
        # 顔箇所を四角で描画
        cv2.rectangle(img, (int(d.left()), int(d.top())), (int(d.right()), int(d.bottom())), (0, 255, 0), 2)
        # 顔だけをファイルに保存
        cv2.imwrite('./result/Dlib_HOG_CSM/' + str(i) + '.png', img)
