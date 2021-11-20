
# これについて

これは岡山大で研究生の課題についてのごく一部の演習課題です。

# 多言語対応

[English](/readme.md) | [中文](/readme_zh.md)

# ファイルツリー

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

# 紹介

## フィルダー1: Face_recognition

これは4週類の顔検出気を使って  
人の顔を検出するプログラムです

1. CNN
2. Dlib_HOG_CSM
3. HAAR_CASCADE
4. MTCNN

## フィルダー2: SLIC

これは、入力した画像から、MTCNNで顔検出して  
その顔領域だけでSLIC(Simple Liner Iterative Clustering)を用いて  
Superpixel化して、40個に分割するというプログラムです

## フィルダー3: F_S

このフィルダーにはは

フィルダー２のこの結果を使って，次の処理を行います．

・superpixel化した40個の各領域において，正方形の小ブロック
で取り出してください．ただし，次の制約条件を満足すること．

- 小ブロックは，その領域の95%以上を含む最小サイズ
- 領域内は元の画像の画素値
- 領域外は，画素値0に置き換え

結果として，一つの顔領域画像から，40個の小画像を出力するということです。