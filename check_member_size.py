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



# 查看和统计表格中的strut尺寸有几种
get = pd.read_excel(io='./tempfile.xlsx',
                    sheet_name='struts',
                    names=['WALL TYPE', 'FORCE PER METER', 'STRUT LAYER', 'STRUT TYPE', 'STRUT SIZE', 'MEMBER TYPE',
                           'DOUBLE', 'CENTER Δ', 'AXIAL FORCE'],
                    usecols='A,D,E,F,G,H,K,L,X',
                    index_col=0,
                    skiprows=0,
                    )
get["STRUT SIZE"] = get["STRUT SIZE"].str.lower()
get["STRUT LAYER"] = get["STRUT LAYER"].fillna(0).astype(int)
get[["DOUBLE", "CENTER Δ"]] = get[["DOUBLE", "CENTER Δ"]].fillna("-")
get["AXIAL FORCE"] = get["AXIAL FORCE"].apply(np.ceil)






if __name__ == "__main__":
    foo_set_option()

    # print(get)
    from collections import Counter
    #
    print(Counter(get["STRUT SIZE"]))


