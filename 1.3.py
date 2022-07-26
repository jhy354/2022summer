#!/usr/bin/env python3

'''
Input:
4
4500
1
9870
1
12890
0
57890
1

Expected Output:
4.1
'''

def calc_t(step : int) -> float:
    t = 0
    if step >= 1000 and step <3000:
        t = 0.3
    elif step >= 3000 and step <=55000:
        t = 0.3 + ((step-1000) // 2000 * 0.1)
    elif step > 55000:
        t = 3
    return t


if __name__ == "__main__":
    total = 0
    c = 0
    
    n = int(input())
    # list count from 1
    for i in range(1, n+1):
        if i <= n:
            x = int(input())
            f = int(input())
            
            if f == 1:
                c += 1
            elif f == 0:
                c = 0
            else:
                exit(1)
            
            if c >= 4:
                total += 2*calc_t(x)
            elif c > 0:
                total += calc_t(x)
        else:
            break

    print(total)

    exit(0)