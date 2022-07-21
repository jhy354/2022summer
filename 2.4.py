#!/usr/bin/env python3

if __name__ == "__main__":
    year = int(input("year:"))
    m = int(input("month:"))
    d = int(input("day:"))

    if m == 1 or m == 2:
        m += 12
    y = year % 100
    c = (year - y)//100
    w = y + (y//4) + (c//4) - (2*c) + (26*(m+1)//10) + d - 1

    weekday = w % 7    
    if weekday == 0:
        print("星期日")
    elif weekday == 1:
        print("星期一")
    elif weekday == 2:
        print("星期二")
    elif weekday == 3:
        print("星期三")
    elif weekday == 4:
        print("星期四")
    elif weekday == 5:
        print("星期五")
    elif weekday == 6:
        print("星期六")
    else:
        exit(1)

    exit(0)