#!/usr/bin/env python3

def func1() -> None:
    a = input("a:")
    b = input("b:")
    # check val type
    print(a in b)
    return


def func2() -> None:
    a = input("a:")
    b = input("b:")
    if a == b:
        print("==")
    if a != b:
        print("!=")
    if a <= b:
        print("<=")
    if a >= b:
        print(">=")
    if a < b:
        print("<")
    if a > b:
        print(">")
    return


if __name__ == "__main__":
    func1()
    func2()
    func2()

    exit(0)
