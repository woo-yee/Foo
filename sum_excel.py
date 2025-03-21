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


foo_set_option()

sheet_name_MS = ["YLBPS 1 (" + str(i) + ")" for i in range(17, 35)] + \
                ["YLBPS 2 (" + str(i) + ")" for i in range(13, 17)] + \
                ["YLBPS 3 (" + str(i) + ")" for i in range(5, 13)] + \
                ["YLBPS 4 (" + str(i) + ")" for i in range(35, 39)]

sheet_name_CS = ["YLBPS_CS (" + str(i) + ")" for i in range(1, 5)] + \
                ["AB (D1)", "AB (E1)"]

# print(sheet_name)
sheet = []
totalloading = []
strutweight = []
for i in sheet_name_MS:
    get = pd.read_excel(io='./Appendix G King Post Design 1 - 0321 - SPT-N - 4mPD.xlsx',
                        sheet_name=i,
                        usecols='A:I',
                        # index_col=0,
                        # skiprows=0,
                        )
    sheet.append(i)
    totalloading.append(get.iloc[28, 8])
    strutweight.append(get.iloc[9, 8])

# print(totalloading)
# print(len(totalloading))


df_MS = pd.DataFrame({"sheet name": sheet,
                      "total loading": totalloading,
                      "strut weight": strutweight})

# print(df)
# print(df["total loading"].max())



sheet = []
totalloading = []
strutweight = []
for i in sheet_name_CS:
    get = pd.read_excel(io='./Appendix G King Post Design 1 - 0321 - SPT-N - 4mPD.xlsx',
                        sheet_name=i,
                        usecols='A:I',
                        # index_col=0,
                        # skiprows=0,
                        )
    sheet.append(i)
    totalloading.append(get.iloc[28, 8])
    strutweight.append(get.iloc[9, 8])

# print(totalloading)
# print(len(totalloading))


df_CS = pd.DataFrame({"sheet name": sheet,
                      "total loading": totalloading,
                      "strut weight": strutweight})



xlsx_name = "output.xlsx"
with pd.ExcelWriter(xlsx_name) as writer:
    try:
        df_MS.to_excel(writer, sheet_name='sum_MS')
        df_CS.to_excel(writer, sheet_name='sum_CS')
    except NameError:
        ex_type, ex_val, ex_stack = sys.exc_info()  # 打印部分信息
        print(str(ex_type) + ": " + str(ex_val))

if __name__ == "__main__":
    foo_set_option()
