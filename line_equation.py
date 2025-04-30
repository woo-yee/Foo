#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File    :line_equation.py
# @Time    :2025/3/26 18:57
# @Author  :Ivan

import numpy as np

a = np.array([109.8, 100, ])
a = np.array([-0.05730, -0.05591, -0.05743, -0.05748, -0.05748, -0.05832, -0.05875, -0.05911, -0.05917, -0.06860, ])
a = a + 0.0074
a[-1] = -0.05489


# a = [-0.05730, -0.05591, -0.05743, -0.05748, -0.05748, -0.05832, -0.05875,-0.05911,-0.05917, -0.06860, ]
# aa = []
# for i in a:
#     aa.append(i + 0.0074)
#     if
#     aa.append(i + 0.0074)

if __name__ == "__main__":
    np.set_printoptions(formatter={'float': '{: 0.5f}'.format})
    print(a.size)
    print(a)
