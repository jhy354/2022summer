#!/usr/bin/env python3


# decorator(多此一举)
def io(func):
    def wrapper():
        num = int(input("number:"))
        num = func(num)
        print(num)
    return wrapper


@io
def sub(num):
    num -= 1
    return num


@io
def time(num):
    num *= 2
    return num


@io
def div(num):
    num /= 2
    return num


@io
def mod(num):
    num %= 2
    return num


if __name__ == "__main__":
    float_ = 26.0
    print(type(float_))
    str_ = "26.0"
    print(type(str_))
    int_ = 1
    print(type(int_))

    sub()
    time()
    div()
    mod()

    exit(0)
