#!/usr/bin/env python3

if __name__ == "__main__":
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    print(a <= b and a <= c)
    print(a <= b <= c or a <= c <= b)
    print(not (a < b))
    
    exit(0)
