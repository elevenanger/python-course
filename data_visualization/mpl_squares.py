# @File  : mpl_squares.py
# @Author: liuanglin
# @Time: 2022/6/29 20:55 
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

ax.set_title("square number", fontsize=24)

plt.show()
