#!/usr/bin/python
# -*- coding:UTF-8 -*-
# @Time:  18:18
# @File: GreekAlphabet.py
# @Software: PyCharm


import pandas as pd
import numpy as np

def alphabet():
    CHAR = [chr(code) for code in range(913, 938)]
    CODElist = [code for code in range(913, 938)]
    char = [chr(code) for code in range(945, 970)]
    codelist = [code for code in range(945, 970)]
    pron = ["alpha", "beta", "gamma", "delta", "epsilon",
            "zeta", "eta", "theta", "iota", "kappa",
            "lambda", "mu", "nu", "xi", "omicron",
            "pi", "rho", np.nan, "sigma", "tau",
            "upsilon", "phi", "chi", "psi", "omega"]
    pronCH = ["阿尔法", "贝塔", "伽马", "德尔塔", "艾普西隆",
              "泽塔", "伊塔", "西塔", "约塔", "卡帕",
              "兰布达", "谬", "纽", "柯西", "奥密克戎",
              "派", "柔", np.nan, "西格玛", "陶",
              "宇普西隆", "佛-爱", "恺", "普赛", "欧米伽"]
    alph_df = pd.DataFrame(data=[CHAR, char, pron, pronCH],
                           index=["uppercase", "lowercase", "pronunciation", "pronunciationCH"],
                           columns=[num + 1 for num in range(len(CHAR))])
    alph_df = alph_df.dropna(axis=1)
    alph_df.columns = [num + 1 for num in range(len(CHAR) - 1)]
    return alph_df


if __name__ == '__main__':
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 对齐
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    # 设置输出右对齐
    pd.set_option('display.unicode.east_asian_width', True)
    # 设置多少列之后换行显示，若数字很大（如1000）则相当于不换行显示
    pd.set_option('display.width', 101)
    # 设置单列宽度
    pd.set_option('max_colwidth', 20)
    alph_df = alphabet()
    print(alph_df)



