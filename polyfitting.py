#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    :line_equation.py
# @Time    :2025/3/26 18:57
# @Author  :Ivan

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'D:/OneDrive - stu.csust.edu.cn/01.工程项目/B001.DC_2022_03 Yuen Long Barrage and Nullah Improvement Schemes/TWD0006 Combined ELS Across Yuen Long Nullah/01.design/PLAXIS result/'
file_name = 'Settlement of Section K-K - Corner Effects - 20250424.xlsx'
get = pd.read_excel(io=file_path + file_name,
                    sheet_name='Settlement G_Last',
                    usecols='B,H',
                    # index_col=0,
                    skiprows=17,
                    nrows=29,
                    )

if __name__ == "__main__":
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


    foo_set_option()

    start = datetime.now()

    X = get.iloc[:, 0]
    Y = get.iloc[:, 1] * (-1)
    x = np.array([1])
    y = np.polyfit(X, Y, 15)
    yy = np.poly1d(y)
    yi = yy(X)
    print(get)
    print(y)
    print(yy)

    xi_dct = {
        'secA1': [np.array([50, 60, 60, 50, 40, 30, 20, 15, 10, 5]),
                  np.array([20, 15, 10, 5])],
        'secM1': [np.array([50, 60, 60, 50, 40, 30, 20, 15, 10, 5]),
                  np.array([20, 15, 10, 5])],
        'secC': [np.array([20, 15, 10, 5])],
        'secD': [np.array([50, 60, 60, 50, 40, 30, 20, 15, 10, 5]),
                  np.array([20, 15, 10, 5])],
        'secE2': [np.array([50, 60, 60, 50, 40, 30, 20, 15, 10, 5]),
                 np.array([20, 15, 10, 5])],
        'secK': [np.array([50, 60, 60, 50, 40, 30, 20, 15, 10, 5]),
                  np.array([20, 15, 10, 5])],
    }
    xi = xi_dct['secK'][1]
    for i in xi:
        y = np.polyfit(X, Y, 15)  # 重新初始化拟合函数
        y[-1] = y[-1] - i * (-1)
        print('---- xi = ' + str(i) + ' ----')
        print(np.roots(y))

    end = datetime.now()
    print('----' * 20)
    print('程序运行时间为: %s Seconds' % (end - start))
    print('----' * 20)

    plt.plot(X, Y, '*', label='original values')
    plt.plot(X, yi, 'r', label='polyfit values')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.legend(loc=2)  # 指定legend在图中的位置，类似象限的位置
    plt.title('polyfitting')
    plt.show()
