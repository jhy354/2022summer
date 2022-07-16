#!/usr/bin/env python3


def divide_line():
    print('-'*20)


if __name__ == "__main__":
    info = ["BH60018", "苹果", 50]
    reversed_info = reversed(info)
    s = "Hello"
    dic = {"铅笔":71, "钢笔":59, "橡皮":98, "尺子":92}
    
    for i in info:
        print(i)
    divide_line()
    
    for i in s:
        print(i)
    divide_line()

    cnt = 0
    for i in reversed(info):
        if cnt >= 2:
            break
        print(i)
        cnt += 1
    divide_line()

    for i in s[1:4]:
        print(i)
    divide_line()

    print(dic["尺子"])
    divide_line()

    exit(0)
