#!/usr/bin/env python3


def divide_line() -> None:
    print('-'*15)
    return


if __name__ == "__main__":
    a = int(input("a:"))
    b = int(input("b:"))

    # swap
    a ^= b
    b ^= a
    a ^= b
    print(f"a = {a}, b = {b}")
    divide_line()
    
    # help
    #help(int())
    #divide_line()

    # str
    s = str(a) + str(b)
    print(f"s = {s}")
    divide_line()

    # ord & chr
    s = "Hello"
    ords0 = ord(s[0])
    ords1 = ord(s[1])
    print(f"s[0] = {ords0}, s[1] = {ords1}")
    print(f"s[0] = {chr(ords0)}, s[1] = {chr(ords1)}")
    divide_line()

    # round
    pi = 3.1415926
    print(f"pi = {round(pi, 2)}")
    divide_line()

    exit(0)
