# What is this?
This is a repository for my project practice as a rearch student in Okayama-U.

# l18i

[中文](/readme_zh.md) | [日本語](/readme_jp.md)

# File Tree

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

# Introduce

## Folder1: Face_recognition

This program used four methods to recognise human face.

1. CNN
2. Dlib_HOG_CSM
3. HAAR_CASCADE
4. MTCNN

## Folder2: SLIC

This code completes the function of super-pixel processing, and is applied to the result recognized by a face detection code form the Folder1.

## Folder3: F_S

The goal of this program is to combine the codes of the first two folders, use the super-pixel processing program to process the face image recognized by the face, and output each pixel block.

The output content is required to retain the content of the original image corresponding to the color, set the color value of other parts to 0, and the pixel in block area is required to occupy at least 95% of the area of the original image which super-pixeled color block pixel has a same color.