#!/usr/bin/env python3

from math import sqrt


def area(a : int, b : int, c : int) -> float:
    p = (a + b + c)/2
    s = sqrt(p * (p-a) * (p-b) * (p-c))
    return s


if __name__ == "__main__":
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    print(area(a, b, c))
    
    exit(0)