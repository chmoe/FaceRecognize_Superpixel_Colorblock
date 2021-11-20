# -*- coding: UTF-8 -*-
# @Project: Face_recognition 
# @File: haar_cascade 
# @Author: rtmacha
# @Date: 2021/09/25 9:06

import cv2  # conda install opencv
import copy

# OpenCV
cascade_fn = "./haarcascade_frontalface_alt.xml"
face_cascade = cv2.CascadeClassifier(cascade_fn)  # 级联分类器（滑动窗口+级联分类器）

for i in range(37):

    img = cv2.imread(r'./picture/' + str(i) + '.jpg')
    img = cv2.resize(img, dsize=(480, 640))

    face_frame = copy.deepcopy(img)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图片
    gray_img = cv2.equalizeHist(gray_img)  # 图片平滑化（直方图均衡化，用于提高图像的质量）

    # 检测出人脸的四个点（起始坐标x,y xy方向的长度）
    dets = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in dets:
        # 顔のトリミング
        face_image = face_frame[y:y + h, x:x + w]
        cv2.putText(img, "Haar", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        # 顔箇所を四角で描画
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 只保存画出的人脸
        cv2.imwrite('./result/haar_face/' + str(i) + '.png', img)
