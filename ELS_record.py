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
    print('---- kickout checking ----')

    lst1 = [['B1', 5, '3000x3000', ],
            ['D1', 1, '5250x4050', ],
            ['C1', 2, '5250x4050, 3000x3000', ],
            ['C2', 4, '4800x3000, 3000x3000', ],
            ['B2', 1, '4800x3000', ],
            ['D2', 1, '5250x4050', ],
            ['B3', 3, '3000x3000', ],
            ['F1', 2, '3000x3000', ]]
    df1 = pd.DataFrame(data=lst1, columns=['type', 'count', 'size'])

    lst2 = [['C3', 2, '4800x3000', ],
            ['C4', 1, '3000x3000', ],
            ['D3', 1, '5250x4050', ],
            ['C2', 4, '4800x3000, 3000x3000', ],
            ['B2', 2, '4800x3000, 3000x3000', ],
            ['C5', 4, '4800x3000, 3000x3000', ],
            ['F2', 2, '4800x3000, 3000x3000', ],
            ['E', 1, '6600x4400', ]]
    df2 = pd.DataFrame(data=lst2, columns=['type', 'count', 'size'])

    lst3 = [['A', 30, 'cut slope', ]]
    df3 = pd.DataFrame(data=lst3, columns=['type', 'count', 'size'])

    print(df1, '\n', df2, '\n', df3)
    return df1, df2, df3


if __name__ == "__main__":
    foo_set_option()

    df1, df2, df3 = main()
    print(df1['count'].sum(), '\t', df2['count'].sum(), '\t', df3['count'].sum())

    df = pd.concat([df1, df2, df3])
    print(df[df['type'].str.contains('B')])

    print('---- ELS design data ----')
    lst = [
        ['A', 'A1', 3000, 224,
         15.80, 15.20, None, None, None, 14.60,
         2.5,
         3.60, 2.01, '>2.0',
         6.3, 1.54, '>1.5',
         2.8, 2.03, '>2.0', ],
        ['B', 'B1/B2/B3', 3000, 120,
         18.61, 16.91, 18.11, None, None, 15.20,
         9.0,
         10.20, 2.27, '>2.0',
         12.11, 1.54, '>1.5',
         10.61, 2.10, '>2.0', ],
        ['C', 'C1/C2/C3', 3000, 53.5,
         33.10, 30.71, 32.60, 29.72, None, 28.31,
         21.0,
         21.81, 3.37, '>2.0',
         25.1, 2.61, '>1.5',
         23.6, 2.82, '>2.0', ],
        ['C', 'C4', 3000, 271.50,
         33.40, 31.48, 32.90, 30.97, None, 29.56,
         21.0,
         23.06, 2.21, '>2.0',
         25.4, 1.65, '>1.5',
         23.4, 2.05, '>2.0', ],
        ['C', 'C5', 3000, 133,
         17.50, 15.51, 17.00, 14.93, None, 13.52,
         21.0,
         7.02, 2.94, '>2.0',
         11.0, 2.03, '>1.5',
         9.5, 2.27, '>2.0', ],
        ['D', 'D1/D2/D3', 3000, 43.5,
         36.40, 33.53, 35.90, 33.98, 32.06, 30.65,
         16.0,
         25.65, 2.43, '>2.0',
         26.9, 2.45, '>1.5',
         24.9, 2.82, '>2.0', ],
        ['E/F', 'E/F1/F2', 3000, 224,
         14.10, 12.49, 13.60, None, None, 10.87,
         8.0,
         3.87, 2.29, '>2.0',
         6.6, 1.56, '>1.5',
         4.6, 2.08, '>2.0', ],
    ]
    df = pd.DataFrame(data=lst, columns=['type', 'design type', 'ELS width', 'surcharge',
                                         'ground level', 'ground water level', 'S1 level', 'S2 level', 'S3 level', 'final excavated level',
                                         'Rockhead Level',
                                         'toe level', 'F.O.S. (Toe Stability)', 'F.O.S. (Hydraulic Stability)',
                                         'optimized 1: toe level', 'optimized 1: F.O.S. (Toe Stability)', 'optimized 1: F.O.S. (Hydraulic Stability)',
                                         'optimized 2: toe level', 'optimized 2: F.O.S. (Toe Stability)', 'optimized 2: F.O.S. (Hydraulic Stability)',
                                         ])
    df['wall length'] = (df['ground level'] - df['toe level']) * 1000
    df['optimized 1: wall length'] = (df['ground level'] - df['optimized 1: toe level']) * 1000
    df['optimized 2: wall length'] = (df['ground level'] - df['optimized 2: toe level']) * 1000
    df['ELS depth'] = (df['ground level'] - df['final excavated level']) * 1000
    # df['embedment length'] = (df['final excavated level'] - df['toe level']) * 1000

    df = df.set_index('type')
    new_columns_order = ['design type', 'ELS width', 'ELS depth', 'surcharge',
                         'ground level', 'ground water level', 'S1 level', 'S2 level', 'S3 level', 'final excavated level',
                         'Rockhead Level',
                         'wall length', 'toe level', 'F.O.S. (Toe Stability)', 'F.O.S. (Hydraulic Stability)',
                         'optimized 1: wall length', 'optimized 1: toe level', 'optimized 1: F.O.S. (Toe Stability)', 'optimized 1: F.O.S. (Hydraulic Stability)',
                         'optimized 2: wall length', 'optimized 2: toe level', 'optimized 2: F.O.S. (Toe Stability)', 'optimized 2: F.O.S. (Hydraulic Stability)',
                         ]
    df_new_order = df.reindex(columns=new_columns_order)
    print(df_new_order)

    time_dt = datetime.now()
    localtime = time_dt.strftime("%Y%m%d-%H%M%S")

    xlsx_name = 'optimized_sheet_pile_wall ' + localtime + '.xlsx'
    with pd.ExcelWriter(xlsx_name) as writer:
        try:
            df_new_order = df_new_order.fillna('/')
            df_output = df_new_order.T
            df_output['unit'] = ['/', 'mm', 'mm', 'kPa',
                                 'mPD', 'mPD', 'mPD', 'mPD', 'mPD', 'mPD',
                                 'mPD',
                                 'mm', 'mPD', '/','/',
                                 'mm', 'mPD', '/','/',
                                 'mm', 'mPD', '/','/',
                                 ]
            df_output.to_excel(writer, sheet_name='FSP')
        except NameError:
            ex_type, ex_val, ex_stack = sys.exc_info()  # 打印部分信息
            print(str(ex_type) + ": " + str(ex_val))
