#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    :HK_plaxis_ELSPRE.py
# @Time    :2023/11/14 14:49
# @Author  :Ivan

from datetime import datetime
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


def main():
    x_ordinate_P = np.array([0, 10500, 16200,
                             11000,
                             16200, 10500])
    x_ordinate = np.array([0, 10500 / 2, 10500 / 2, 16200 / 2, 16200 / 2,
                           11000 / 2, 11000 / 2,
                           16200 / 2, 16200 / 2, 10500 / 2, 10500 / 2])
    y_ordinate = np.array([0, 5500,
                           5000, 9000, 9000, 9000, 9000,
                           7700, 9000, 9000, ])
    z_ordinate = np.array([0, 9000, 500])
    for i in [x_ordinate_P, x_ordinate, y_ordinate, z_ordinate]:
        print(np.cumsum(i))


def formatprint(one, title="ing", ):
    # --------------------------------------------------------------------------------------------------------------------------------
    print("----" * 4 + title + "----" * 4)
    print(one)
    print("----" * 30)


def space_linear_equation(point_ary, x=None, y=None, z=None, on=False):
    x0, y0, z0 = point_ary[0, 0], point_ary[0, 1], point_ary[0, 2]
    # x1, y1, z1 =  point_ary[1, 0], point_ary[1, 1], point_ary[1, 2]
    # 计算直线的方向向量
    direction_vector = point_ary[1] - point_ary[0]
    # 计算直线上的坐标
    if y == None and z == None:
        t = (x - x0) / direction_vector[0]
        y = y0 + direction_vector[1] * t
        z = z0 + direction_vector[2] * t
    elif z == None and x == None:
        t = (y - y0) / direction_vector[1]
        z = z0 + direction_vector[2] * t
        x = x0 + direction_vector[0] * t
    elif x == None and y == None:
        t = (z - z0) / direction_vector[2]
        x = x0 + direction_vector[0] * t
        y = y0 + direction_vector[1] * t
    else:
        print("only need one of x, y, z")
    if on:
        formatprint("expression: (x-{})/{} = (y-{})/{} = (z-{})/{}".format(
            x0, direction_vector[0],
            y0, direction_vector[1],
            z0, direction_vector[2], ), "space_linear_equation")
    return x, y, z


if __name__ == "__main__":
    foo_set_option()

    main()

    print('--------第1跨--------')
    x_ary = np.cumsum(np.array([0, 1.75, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 1.75]))
    print(x_ary)
    x, y, z = space_linear_equation(np.array([(0, 0, 9), (10.5 / 2, 0, 9.5)]), x=x_ary, on=True)
    print(x, y, z)
    print(z - 9)

    print('--------第2跨--------')
    x_ary = np.cumsum(np.array([0, 1.6, 1.5, 1.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.6]))
    print(x_ary)
    x_ary += 10.5
    print(x_ary)
    x, y, z = space_linear_equation(np.array([(10.5, 0, 9), (10.5 + 16.2 / 2, 0, 9.5)]), x=x_ary, on=True)
    print(z - 9)

    print('--------第3跨--------')
    x_ary = np.cumsum(np.array([0, 0.5, 1.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 1.5, 0.5]))
    print(x_ary)
    x_ary += 10.5 + 16.2
    print(x_ary)
    x, y, z = space_linear_equation(np.array([(10.5 + 16.2, 0, 9), (10.5 + 16.2 + 11 / 2, 0, 9.5)]), x=x_ary, on=True)
    print(z - 9)


    def aaa(x):
        b = 1*(x==1) + 2*(x==20) + 3*(x<1)+4*(x>20)
        print(b)

    aaa(-100)

    # 先定义测试用的变量，分别是字符串、整型、浮点型、np.array、pd.DataFrame
    aa = 'weqweqw'
    bb = 4565
    cc = 546.5
    dd = np.array([bb, cc])
    ff = pd.DataFrame([dd, dd[::-1]])

    # 放到列表里，方便后续在循环中使用
    test = [aa, bb, cc, dd, ff]

    vname = lambda v, nms: [vn for vn in nms if id(v) == id(nms[vn])][0]
    print(vname(test))
    
