# -*- coding: UTF-8 -*-
# @Project: Progress 
# @File: color 1
# @Author: Henry Wu 
# @Date: 2021/10/12 9:30
import math

import cv2
import numpy as np
import os


class ColorProcessor(object):

    def __init__(self, file_path, source_file_path):
        self.source_file = self.open_image(source_file_path)
        self.data = self.open_image(file_path)
        self.image_height = self.data.shape[0]  # 图片高度 341
        self.image_width = self.data.shape[1]  # 图片宽度 266
        self.img_ndarray = np.full((self.image_height, self.image_width), '0000000')  # 建立一个图片大小的二维数组，用0初始化

        self.last_color = "#"  # 存储上一个颜色（在循环过程中为当前颜色）
        self.color_set = set()  # 创建一个集合用于不重复存储当前颜色的位置

        # 当前颜色范围
        self.most_left = self.image_width
        self.most_right = 0
        self.most_top = self.image_height
        self.most_bottom = 0

        self.color_count = 0

    @staticmethod
    def open_image(path):
        """
        打开图片
        Return:
            高(row), 宽(col), 颜色([rgb])
        """
        # rgb = cv2.imread(path)[:, :, (2, 1, 0)]  # BGR转换为RGB（效果同下）
        bgr = cv2.imread(path)
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)  # BGR转换为RGB
        return rgb  # shape=(341, 266, 3)

    @staticmethod
    def rgb2hex(rgb):
        hex_color = '#'
        for i in rgb:
            num = int(i)
            # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
            hex_color += str(hex(num))[-2:].replace('x', '0').upper()
        return hex_color

    def traversal(self, i):
        """
        遍历数组
        :return:
        """
        counter = 0
        for row in range(self.image_height):
            for col in range(self.image_width):
                if self.img_ndarray[row, col] != '0000000':  # 当之前有过标注时
                    pass
                else:  # 当没有标注时
                    self.last_color = self.rgb2hex(self.data[row, col])  # 保存当前的hex颜色值
                    self.img_ndarray[row, col] = self.last_color  # 在ndarray中标记颜色的值

                    self.get_connected(row, col)  # 遍历找到当前点的连通区域

                    point = self.move_rectangle()  # 上下左右

                    print("point: \n", point)
                    if point:
                        path = "./Process_result1/{}_{}.png".format(i, counter)
                        print("last_color: {}".format(self.last_color))
                        self.save_image(path, point)
                        counter += 1

    def save_image(self, path, point):
        """
        按照要求处理图片，然后进行保存
        :param path: 图片保存路径
        :param point: 上下左右的限定范围
        :return:
        """
        data_copy = self.source_file[point[0]:point[1], point[2]:point[3], :]

        for row in range(point[0], point[1]):
            for col in range(point[2], point[3]):
                # print("row: {}, col: {}".format(row, col))
                if self.img_ndarray[row, col] == self.last_color:
                    continue
                else:
                    data_copy[row - point[0]][col - point[2]] = (0, 0, 0)  # 将RGB通道设置为0

        cv2.imwrite(path, data_copy[:, :, (2, 1, 0)])

    def move_rectangle(self):
        """
        使用矩形在范围内移动，并且逐渐扩大巨星以找到最大结果
        :return: 返回 上下左右
        """
        min_sqa = math.ceil(self.color_count * 0.95)  # 最小像素数
        print("最小像素数: ", min_sqa)
        min_rec = math.ceil(math.sqrt(min_sqa))  # 最小正方形边长（颜色块数的95%）向上取整
        width = self.most_right - self.most_left  # 宽度
        height = self.most_bottom - self.most_top  # 长度
        max_rec = max(width, height)  # 最大正方形边长
        count = 0  # 当前滑动窗口中同样颜色元素的个数
        print("mo_le: {}, mo_ri: {}, mo_to: {}, mo_bo: {}".format(self.most_left, self.most_right, self.most_top, self.most_bottom))
        print("min_rec: {}, max_rec: {}".format(min_rec, max_rec))
        for d in range(min_rec, max_rec + 1):
            print("width: {}, height: {}, d: {}".format(width, height, d))
            if d > width:  # 宽度不够
                for y in range(height - d):
                    for row in range(self.most_top + y, self.most_top + y + d + 1):
                        for col in range(self.most_left, self.most_right + 1):
                            if self.img_ndarray[row, col] == self.last_color:
                                count += 1
                    if count >= min_sqa:
                        return [self.most_top + y, self.most_top + y + d,
                                self.most_left if self.most_left + d <= self.image_width else self.most_right - d,
                                self.most_left + d if self.most_left + d <= self.image_width else self.most_right]
            elif d > height:  # 高度不够
                for x in range(width - d):
                    for row in range(self.most_top, self.most_bottom + 1):
                        for col in range(self.most_left + x, self.most_left + x + d + 1):
                            if self.img_ndarray[row, col] == self.last_color:  # 当前框中颜色是当前颜色
                                count += 1
                    if count >= min_sqa:
                        return [self.most_top if self.most_top + d <= self.image_height else self.most_bottom - d,
                                self.most_top + d if self.most_top + d <= self.image_height else self.most_bottom,
                                self.most_left + x, self.most_left + x + d]
            else:
                for x in range(width - d + 1):
                    for y in range(height - d + 1):
                        for row in range(self.most_top + y, self.most_top + y + d + 1):
                            for col in range(self.most_left + x, self.most_left + x + d + 1):
                                # print("ndarry: {}, last_color: {}".format(self.img_ndarray[row, col], self.last_color))
                                if self.img_ndarray[row, col] == self.last_color:
                                    count += 1
                        print("count: {}, min_sqa: {}".format(count, min_sqa))
                        if count >= min_sqa:
                            return [self.most_top + y, self.most_top + y + d, self.most_left + x, self.most_left + x + d]

    def get_connected(self, _row, _col):
        """
        在图片中从当前点寻找连通域，并且在ndarray中标注颜色
        :param _row: 坐标x
        :param _col: 坐标y
        :return:
        """
        self.color_set = set()  # 创建一个集合用于不重复存储当前颜色的位置
        self.color_set.add((_row, _col))  # 将当前的内容添加到set中

        self.most_left = self.image_width
        self.most_right = 0
        self.most_top = self.image_height
        self.most_bottom = 0

        self.color_count = 0

        while 0 != len(self.color_set):
            # print("循环中, len(set): {}".format(len(self.color_set)))
            [row, col] = self.color_set.pop()  # 从里面随机找一个，并且删除
            # print("row: {}, col: {}".format(row, col))
            # print("color: {}".format(self.rgb2hex(self.data[row, col])))
            self.color_count += 1  # 存储当前颜色的个数
            # 依次遍历上下左右
            if row - 1 >= 0:
                self.set_color(row - 1, col)
            if row + 1 <= self.image_height - 1:
                self.set_color(row + 1, col)
            if col - 1 >= 0:
                self.set_color(row, col - 1)
            if col + 1 <= self.image_width - 1:
                self.set_color(row, col + 1)

    def set_color(self, row, col):
        if self.rgb2hex(self.data[row, col]) == self.last_color:  # 属于当前颜色
            # print("data_col: {}, last_color:{}".format(self.rgb2hex(source_file[row, col]), self.last_color))
            if self.img_ndarray[row, col] != self.last_color:  # 并且没有标记
                # print("没有标记")
                self.img_ndarray[row, col] = self.last_color
                self.color_set.add((row, col))
                if row > self.most_bottom:
                    self.most_bottom = row
                if row < self.most_top:
                    self.most_top = row
                if col < self.most_left:
                    self.most_left = col
                if col > self.most_right:
                    self.most_right = col


if __name__ == '__main__':
    for i in range(37):
        print("第{}/{}个正在运行".format(i + 1, 37))
        p = ColorProcessor('./SLIC_result/{}.png'.format(i), './result/{}.png'.format(i))
        p.traversal(i)
