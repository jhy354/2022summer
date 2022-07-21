#!/usr/bin/env python3

if __name__ == "__main__":
    arr = [71, 59, 98, 92]
    for i in arr:
        print(i)

    for i in range(9, -1, -1):
        print(i)

    sum = 0
    for i in arr:
        sum += i
    print(sum)

    exit(0)