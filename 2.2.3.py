#!/usr/bin/env python3

from random import randint

if __name__ == "__main__":
    ans = randint(0, 100)
    chance = int(input("chance:"))

    while True:
        if chance <= 0:
            print("你输了")
            exit(0)

        a = int(input("请输入猜测的数:"))

        if a == ans:
            break
        elif a < ans:
            print("偏小")
        else:
            print("偏大")

        chance -= 1

    print("正确")

    exit(0)