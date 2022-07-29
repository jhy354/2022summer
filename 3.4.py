#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import codecs
from matplotlib.font_manager import FontProperties

# 太长了
fx = ["欧阳", "太史", "端木", "上官", "司马", "东方", "独孤", "南宫"]
xing = []

if __name__ == "__main__":
    file = codecs.open("xm.csv", 'r', 'utf-8')
    for line in file:
        if line[0:2] in fx:
            xing.append(line[0:2])
        else:
            xing.append(line[0:1])
    
    data = {"xing":xing, "renshu":0}
    df = pd.DataFrame(data)
    s = df.groupby("xing").count()
    s = s.sort_values("renshu", ascending=False)
    ax = s[0:20].plot(kind="bar", rot=0)
    font = FontProperties(fname=r"c:/windows/fonts/simsun.ttc", size=12)
    for label in ax.get_xticklabels():
        label.set_fontproperties(font)
    
    plt.show()
    print(s)
            
    exit(0)