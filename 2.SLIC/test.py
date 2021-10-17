# -*- coding: UTF-8 -*-
# @Project: SLIC 
# @File: test 
# @Author: Henry Wu 
# @Date: 2021/09/28 11:17
from skimage import io, color


rgb_img = io.imread('./result/0.png')
lab_img = color.rgb2lab(rgb_img)

print(rgb_img.shape)
print(lab_img.shape)

print(rgb_img[2])


label = {}
# label[(1,4)] = "你好"
label["你好"] = (1, 4)

print((1,4) in label)
# print(lab_img)


# io.imsave('./0.png', lab_img)