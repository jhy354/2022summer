#!/usr/bin/env python3

if __name__ == "__main__":
    a = int(input("a:"))
    if 90 <= a and a <= 100:
        print("A")
    elif 80 <= a and a <= 89:
        print("B")
    elif 70 <= a and a <= 79:
        print("C")
    elif 60 <= a and a <= 69:
        print("D")
    elif 0 <= a and a <= 59:
        print("E")
    else:
        print("ERROR NUMBER")
        exit(1)
    
    exit(0)