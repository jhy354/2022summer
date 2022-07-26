#!/usr/bin/env python3

from pandas import Series

if __name__ == "__main__":
    s1 = Series([71, 59, 98, 92])
    s2 = Series([71, 59, 98, 92], index=["s01", "s02", "s03", "s04"])
    
    index = 0
    for i in [17, 95, 89, 29]:
        s1[index] = i
        s2[f"s0{index + 1}"] = i
        index += 1

    for i in s1.index:
        print(i)
    for i in s1.values:
        print(i)

    for i in s2.index:
        print(i)
    for i in s2.values:
        print(i)

    exit(0)