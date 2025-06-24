#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    :matplotlib_case.py
# @Time    :2025/06/18 08:17
# @Author  :Ivan

from datetime import datetime
import numpy as np
from numpy import radians, pi, sin, cos, tan, sinh, cosh, tanh, exp
import pandas as pd
import matplotlib.pyplot as plt

# 让图片显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 让图片显示负号
plt.rcParams['axes.unicode_minus'] = False


# # 支持svg矢量图
# %config Inlinebackend.figure_format = ' svg'

# 查看电脑中的字体
def check_fonts():
    from matplotlib.font_manager import FontManager

    fm = FontManager()
    my_fonts = set(f.name for f in fm.ttflist)
    print(my_fonts)


# check_fonts()


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


# 基本绘图
def basic_plot():
    # 抛物线
    x = np.linspace(-5, 5, 50)
    y = x ** 2

    # 画图: 线形图， 折线图
    ## color, line style
    plt.plot(x, y, c='r', ls='-.')
    plt.plot(x, -y, 'b--')

    plt.show()


# 配置画布
def set_figure():
    # figsize: 宽高
    # dpi: 分辨率
    plt.figure(figsize=(6, 3), dpi=100, facecolor='#f1f1f1')

    # 正弦曲线
    x = np.linspace(0, 4 * pi)
    y = sin(x)

    # 画图: 线形图， 折线图
    ## color, line style
    plt.plot(x, y, c='r')
    plt.plot(x, -y, c='b', ls='--')
    plt.plot(x, cos(x), c='g', ls='-.')

    # 设置网格
    plt.grid()

    plt.show()


# 布局多图, 方法1
def make_plots_1():
    # figsize: 宽高
    # dpi: 分辨率
    fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#f1f1f1')

    # 正弦曲线
    x = np.linspace(-pi, pi, 30)
    y = sin(x)

    # 子图1
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(x, y, c='b', ls='--')
    ax1.set_title('子图1')

    # 子图2
    ax2 = plt.subplot(2, 2, 2)
    ax2.plot(x, -y, c='r', ls='-')
    ax2.set_title('子图2')

    # 子图3
    ax3 = plt.subplot(2, 2, 3)
    ax3.plot(x, -y, c='g', ls='-.')
    ax3.set_title('子图3')

    # 子图4
    ax4 = plt.subplot(2, 2, 4)
    ax4.plot(x, y, c='c', ls=':')
    ax4.set_title('子图4')

    # 自动调整布局
    fig.tight_layout()

    # 设置网格
    plt.grid()

    plt.show()


# 布局多图, 方法2
def make_plots_2():
    # figsize: 宽高
    # dpi: 分辨率
    fig = plt.figure(figsize=(8, 5), dpi=100, facecolor='#f1f1f1')

    # 正弦曲线
    x = np.linspace(-pi, pi, 30)
    y = sin(x)

    # 子图1
    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(x, y, c='b', ls='--')
    ax1.set_title('子图1')

    # 子图2
    ax2 = plt.subplot(2, 2, 2)
    ax2.plot(x, -y, c='r', ls='-')
    ax2.set_title('子图2')

    # 子图3
    ax3 = plt.subplot(2, 1, 2)
    ax3.plot(x, -y, c='g', ls='-.')
    ax3.set_title('子图3')

    # 自动调整布局
    fig.tight_layout()

    # 设置网格
    plt.grid()

    plt.show()


# 布局多图, 方法3
def make_plots_3():
    x = np.linspace(0, 2 * pi)

    # 3行3列
    fig, axes = plt.subplots(3, 3)
    ax1, ax2, ax3 = axes
    ax11, ax12, ax13 = ax1
    ax21, ax22, ax23 = ax2
    ax31, ax32, ax33 = ax3

    # fig设置画布大小
    fig.set_figwidth(12)
    fig.set_figheight(8)

    ax11.plot(x, sin(x))
    ax12.plot(x, cos(x))
    ax13.plot(x, tan(x))

    ax21.plot(x, sinh(x))
    ax22.plot(x, cosh(x))
    ax23.plot(x, tanh(x))

    ax31.plot(x, sin(x) + cos(x))
    ax32.plot(x, sin(x) ** 2 + cos(x) ** 2)
    ax33.plot(x, 1 / sin(x) + 1 / cos(x))

    # 自动调整布局
    fig.tight_layout()

    # 设置网格
    plt.grid()

    plt.show()


# 布局多图(嵌套图), 方法4
def make_plots_4():
    x = np.linspace(0, 2 * pi)

    # 3行3列
    fig = plt.figure(figsize=(8, 5), dpi=100, facecolor='#f1f1f1')

    # 图1
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(x, sin(x))

    # 嵌套图
    ax2 = fig.add_subplot(2, 2, 2, facecolor='pink')
    ax2.plot(x, cos(x))

    # 自动调整布局
    fig.tight_layout()

    # 设置网格
    plt.grid()

    plt.show()


# 布局多图(嵌套图), 方法5
def make_plots_5():
    x = np.linspace(0, 2 * pi, 30)

    # 3行3列
    fig = plt.figure(figsize=(8, 5), dpi=100, facecolor='#f1f1f1')

    # 图1
    plt.plot(x, sin(x))

    # 嵌套图1
    ax1 = plt.axes([0.55, 0.55, 0.3, 0.3])
    ax1.plot(x, sin(x), c='g')

    # 嵌套图2
    ax2 = fig.add_axes([0.18, 0.18, 0.3, 0.3])
    ax2.plot(x, cos(x), c='r')

    plt.show()


# 双轴显示
def set_more_axes():
    x = np.linspace(0, 10, 100)

    fig = plt.figure(figsize=(8, 5), dpi=100, facecolor='#f1f1f1')

    # 图1
    ## 得到当前轴域
    ax1 = plt.gca()
    ax1.plot(x, exp(x), c='b')
    ax1.set_xlabel('time')
    ax1.set_ylabel('$e^x$', c='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # 图2
    ## 和图1共享x轴
    ax2 = ax1.twinx()
    ax2.plot(x, sin(x), c='r')
    ax2.set_ylabel('$sinx$', c='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.tight_layout()

    plt.show()


# 图例
def set_legend():
    x = np.linspace(0, 2 * pi)

    fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#f1f1f1')
    plt.plot(x, sin(x))
    plt.plot(x, cos(x))

    # ncol: 显示成几列
    plt.legend(['sinx', 'cosx'], fontsize=12, loc='center', ncol=2,
               bbox_to_anchor=[0, 1, 1, 0.2])
    plt.tight_layout()

    plt.show()


# 线条属性
def set_lineprops():
    x = np.linspace(0, 2 * pi, 10)

    fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#f1f1f1')
    # c: 颜色
    # marker: 标记
    # ls: line style 线型
    # lw: line width 线宽
    # label: 标签
    # mfc: maker facecolor 标记的背景颜色
    # markersize: 标记的大小
    # markeredgecolor: 标记(点)的边缘颜色
    # alpha: 透明度, 0~1
    plt.plot(x, sin(x), c='r', marker='o', ls='--', lw=1, label='sinx', mfc='y', markersize=10)
    plt.plot(x, cos(x), c='b', marker='*', ls=':', lw=2, label='cosx', mfc='g', markersize=10)
    plt.plot(x, sin(x) - cos(x), c='y', marker='v', ls='-.', lw=1.5, label='sinx-cosx', mfc='r',
             markersize=10)
    plt.plot(x, sin(x) + cos(x), c='k', marker='^', ls='-.', lw=1.5, label='sinx+cosx', mfc='b',
             markersize=10, markeredgecolor='w', alpha=0.5)

    plt.legend()
    plt.tight_layout()

    plt.show()


# 坐标轴的刻度
def set_ticks():
    x = np.linspace(0, 10)

    fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#f1f1f1')
    plt.plot(x, sin(x))

    # ticks: 刻度值, 实际画的数值
    # labels: 显示的刻度标签
    # ha: 水平方向的对齐方式, 一般是right
    plt.xticks(ticks=np.arange(0, 11, 1), fontsize=12, color='r')
    plt.yticks(ticks=[-1, 0, 1], labels=['min', '0', 'max'], fontsize=12, color='b',
               ha='right')

    plt.tight_layout()

    plt.show()


# 坐标轴的范围和配置1
def set_tick_lim1():
    x = np.linspace(0, 2 * pi)

    fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#f1f1f1')
    plt.plot(x, sin(x), c='r')

    plt.xlim(-2, 8)
    plt.ylim(-2, 2)

    plt.tight_layout()

    plt.show()


# 坐标轴的范围和配置2
def set_tick_lim2():
    x = np.linspace(0, 2 * pi)

    fig = plt.figure(figsize=(6, 4), dpi=100, facecolor='#f1f1f1')
    plt.plot(x, sin(x), c='r')

    # 设置坐标轴范围: [xmin, xmax, ymin, ymax]
    plt.axis([-2, 8, -2, 2])
    # option
    ## off: 不显示坐标轴
    ## equal: 让x轴和y轴的刻度距离相同
    ## scaled: 自动缩放坐标轴和图片匹配
    ## tight: 紧凑型自动适配图片
    ## square: 让画布呈现正方形，x轴和y轴宽高一致
    plt.axis('scaled')

    plt.tight_layout()

    plt.show()


# 设置标题和网格
def set_title__grid():
    x = np.linspace(0, 2 * pi)

    fig = plt.figure(figsize=(6, 5), dpi=100, facecolor='#f1f1f1')
    plt.plot(x, sin(x), c='r')

    # 图的标题
    plt.title('sin曲线', fontsize=20, loc='center')
    plt.suptitle('父标题', fontsize=24, y=1)

    # 网格线
    ## ls: line style
    ## lw: line width
    ## axis: 让哪个轴显示网格线, x, y, both
    plt.grid(ls='--', lw=0.5, c='gray', axis='both')

    plt.show()


# 设置标签
def set_label():
    x = np.linspace(0, 2 * pi)

    fig = plt.figure(figsize=(10, 5), facecolor='#f1f1f1')
    plt.plot(x, sin(x), c='r')

    # 坐标轴标签
    ## rotation: 旋转角度, xlabel默认0 deg, ylabel默认90 deg
    plt.xlabel('y=sinx', fontsize=12)
    plt.ylabel('y=sinx', fontsize=12, rotation=0, horizontalalignment='right')
    plt.title('正弦曲线')

    plt.show()


# 设置文本
def set_text():
    x = np.linspace(1, 10, 10)
    y = np.array([10, 50, 30, 50, 80, 90, 10, 20, 50, 30])

    fig = plt.figure(figsize=(6, 4), facecolor='#f1f1f1')
    plt.plot(x, y, c='r', ls='--', marker='o')

    # 画文字
    ## s: 文本内容
    ## ha: 水平对齐方式
    ## va: 垂直对齐方式
    for a, b in zip(x, y):
        plt.text(x=a + 0.1, y=b + 0.1, s=b, fontsize=10, color='b',
                 ha='left', va='bottom')

    plt.show()


# 设置标注
def set_annotate():
    x = np.linspace(1, 10, 10)
    y = np.array([10, 50, 30, 50, 50, 60, 10, 20, 50, 30])

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.plot(x, y, c='r', ls='--', marker='o')

    # 画标注或注释
    ## text: 标注内容
    ## xytext: 标注内容的位置: 箭头的起始位置
    ## xy: 标注的坐标点: 箭头指向的位置
    ## arrowprops: 箭头属性
    ### width: 箭头线的宽度
    ### headwidth: 箭头头部的宽度
    ### facecolor: 箭头的背景颜色
    for a, b in zip(x, y):
        plt.annotate(text='最高销量', xytext=(a + 0.5, b + 3), xy=(a, b), fontsize=10, color='b',
                     arrowprops={'width': 0.75, 'headwidth': 5, 'facecolor': 'gray'})

    plt.show()


# 保存图片
def save_fig():
    x = np.linspace(1, 10, 10)
    y = np.array([10, 50, 30, 50, 50, 60, 10, 20, 50, 30])

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.plot(x, y, c='r', ls='--', marker='o')

    plt.show()

    plt.savefig(fname='test.png', dpi=100, facecolor='pink', pad_inches=1)


# 折线图
def line_chart():
    x = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    y = [10, 50, 60, 10, 20, 50, 30]

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.plot(x, y, c='r', ls='--', marker='D', markersize=5)

    plt.xlabel('weeks')
    plt.ylabel('activity')
    plt.title('Python')

    # 文本
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='left', va='bottom')

    x = np.random.randint(0, 10, size=15)

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.plot(x, c='r', ls='--', marker='d', markersize=5)
    plt.plot(x.cumsum(), c='b', ls=':', marker='o', markersize=5)

    plt.show()


# 柱状图或条形图
def bar_chart():
    x = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    y = [10, 50, 60, 10, 20, 50, 30]

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.bar(x, y, width=0.5)

    # 在每个柱子上显示数值
    for a, b in zip(x, y):
        plt.text(a, b, s='{:.1f}万'.format(b / 10),
                 ha='center', fontsize=8)

    plt.xlabel('weeks')
    plt.ylabel('activity')
    plt.title('Python')

    # 簇状柱状图
    x = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
    y1 = np.array([120, 550, 460, 120, 250, 540, 130])
    y2 = np.array([112, 51, 620, 103, 240, 550, 360])
    y3 = np.array([103, 450, 650, 106, 207, 580, 630])

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    w = 0.2
    plt.bar(x - w, y1, width=w, label='北区')
    plt.bar(x, y2, width=w, label='中区')
    plt.bar(x + w, y3, width=w, label='南区')

    plt.legend()

    # 堆叠柱状图
    x = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
    y1 = np.array([120, 550, 460, 120, 250, 540, 130])
    y2 = np.array([112, 51, 620, 103, 240, 550, 360])
    y3 = np.array([103, 450, 650, 106, 207, 580, 630])

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.bar(x, y1, label='北区')
    plt.bar(x, y2, label='中区', bottom=y1)
    plt.bar(x, y3, label='南区', bottom=y1 + y2)

    plt.legend()

    # 条形图
    x = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
    y = np.array([120, 550, 460, 120, 250, 540, 130])

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    plt.barh(x, y, label='北区')

    plt.legend()

    plt.show()


# 直方图
def histogram_chart():
    x = np.random.randint(0, 10, 100)
    # 统计每个数出现的次数
    vc = pd.Series(x).value_counts()
    print(vc)

    fig = plt.figure(figsize=(8, 6), facecolor='#f1f1f1')
    # bins: 组数
    # plt.hist(x, bins=[0, 3, 6, 9, 10],)
    # density: 概率分布, 将y坐标改为0~1的数
    plt.hist(x, bins=10,
             facecolor='b', alpha=0.4, edgecolor='k',
             density=True)
    plt.xticks(range(10))

    plt.show()


if __name__ == "__main__":
    foo_set_option()

    # basic_plot()
    # set_figure()
    # make_plots_1()
    # make_plots_2()
    # make_plots_3()
    # make_plots_4()
    # make_plots_5()
    # set_more_axes()
    # set_legend()
    # set_lineprops()
    # set_ticks()
    # set_tick_lim1()
    # set_tick_lim2()
    # set_title__grid()
    # set_label()
    # set_text()
    # set_annotate()
    # save_fig()
    # line_chart()
    # bar_chart()
    histogram_chart()
