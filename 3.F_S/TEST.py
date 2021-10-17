# -*- coding: UTF-8 -*-
# @Project: 3.F_S 
# @File: TEST 
# @Author: Henry Wu 
# @Date: 2021/10/02 11:42

from skimage import color, io
import cv2



rgb_s = cv2.imread("./result/0.png")

rgb_c = io.imread("./result/0.png")


def rgb2hex(rgb):
    print("转换")
    hexcolor = '#'
    for i in rgb:
        num = int(i)
        # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
        hexcolor += str(hex(num))[-2:].replace('x', '0').upper()
    return hexcolor


print(rgb2hex(rgb_s.shape))

print(rgb_s.shape)

for i in range(0):
    print(i)

# print(RGB_to_Hex(str(rgb[100,199])))
# print(RGB_to_Hex((rgb[100,199]).tolist()))

import numpy as np
x = [[1, 2, 3], [4, 5, 6]]
y = np.copy(x)
y[0][0] = 999
print(x)