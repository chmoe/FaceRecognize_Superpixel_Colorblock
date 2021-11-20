
# 這個倉庫
本倉庫保存了有關人臉識別、超像素化處理等內容的相關代碼，是我的研究生課題練習的一部分代碼。

# 多語言

[English](/readme.md) | [日本語](/readme_jp.md)

# 文件樹

```tree
.
├── 1.Face_recognition
│   ├── CNN.py
│   ├── Dlib_HOG_CSM.py
│   ├── MTCNN.py
│   ├── crawl.py
│   ├── haar_cascade.py
│   ├── haarcascade_frontalface_alt.xml
│   ├── mmod_human_face_detector.dat
│   ├── picture
│   └── result
├── 2.SLIC
│   ├── MTCNN.py
│   ├── SLIC.py
│   ├── SLIC_result
│   ├── picture
│   ├── result
│   └── test.py
├── 3.F_S
│   ├── Process_result
│   ├── SLIC.py
│   ├── SLIC1.py
│   ├── SLIC_result
│   ├── TEST.py
│   ├── color.py
│   └── result
├── readme.md
├── readme_cn.md
└── readme_jp.md
```

# 項目介紹

## 文件夾1: Face_recognition

該文件夾的目的是使用如下四種不同的方式進行人臉識別的操作。

1. CNN
2. Dlib_HOG_CSM
3. HAAR_CASCADE
4. MTCNN

## 文件夾2: SLIC

該代碼實現了超像素化這一功能，並且將該方法應用於文件夾1中處理好的人臉圖像，輸出相應的超像素化後的圖像。

## 文件夾3: F_S

本程序的目標是將前兩個文件夾的程序進行融合，使用超像素化方法處理人臉識別後的圖片。

對於超像素化處理後輸出的結果圖像進行按照顏色進行分隔，將分割後的每一個像素塊進行處理，找到一個正方形能夠框柱該像素塊對應的顏色的像素的至少95%的像素，然後將原圖中這一個方塊的內容進行輸出，輸出時，對應顏色的像素點需要保留原圖像的顏色值，其他顏色的像素需要將其顏色信息設置為0（即將圖像顏色置為黑色）。
