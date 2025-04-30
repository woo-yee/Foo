#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    :HK_plaxis_ELSPRE.py
# @Time    :2023/11/14 14:49
# @Author  :Ivan

import numpy as np
from numpy import cos, radians, pi
import pandas as pd


def foo_set_option():
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 对齐
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    # 设置输出右对齐
    pd.set_option('display.unicode.east_asian_width', True)
    # 设置多少列之后换行显示，若数字很大（如1000）则相当于不换行显示
    pd.set_option('display.width', 110)
    # 设置单列宽度
    pd.set_option('max_colwidth', 200)


def formatprint(one, title="ing", ):
    # --------------------------------------------------------------------------------------------------------------------------------
    formatprint("----" * 4 + title + "----" * 4)
    formatprint(one)
    formatprint("----" * 30)


# 假设螺栓的位置数据为二维坐标点，例如：
# 每一行是一个螺栓的位置，[x, y]
bolts = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

# 计算形心（质心）
centroid_x = np.mean(bolts[:, 0])
centroid_y = np.mean(bolts[:, 1])

print(f"螺栓形心坐标为：({centroid_x}, {centroid_y})")
print(f"螺栓形心坐标为：({centroid_x}, {centroid_y})")

# 生成随机数组
random_array = np.random.uniform(0.04654, 0.05362, 5)
print(random_array)

# 对随机数组进行排序
sorted_array = np.sort(random_array)
print(np.round(sorted_array, 5))

if __name__ == "__main__":
    foo_set_option()

    x = np.array([-30.5, 3.6])
    y = np.array([0, 1])
    xi = np.interp([-1.5, 1.31], x, y)
    print("wave", xi)
    xi = np.interp([1.31, 3.6], x, y)
    print("wind", xi)
    xi = np.interp([-2.5, 3.6], x, y)
    print("stream flow", xi)

    print(1111)

    chars = [chr(i) for i in range(65, 91)]

    sec_lst = ['sec' + i for i in chars]
    print(sec_lst )



