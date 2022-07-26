#!/usr/bin/env python3

from random import *

if __name__ == "__main__":
    print(random())
    
    a = float(input("a:"))
    b = float(input("b:"))
    print(uniform(a, b))

    a = int(input("a:"))
    b = int(input("b:"))
    print(randint(a, b))

    arr = [71, 59, 98, 92]
    n = int(input("n:"))
    for i in range(n):
        index = randint(0, 4)
        print(arr[index])

    exit(0)