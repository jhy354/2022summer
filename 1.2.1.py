#!/usr/bin/env python3

from math import sqrt

if __name__ == "__main__":
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    delta = b**2 - 4*a*c

    if a == 0:
        print("The arg 'a' cannot be 0!")
        exit(1)
    
    ans = []
    solution = None
    if delta == 0:
        solution = 1
        ans.append( (-b + sqrt(delta)) / (2*a) ) 
    elif delta > 0:
        solution = 2
        ans.append( (-b + sqrt(delta)) / (2*a) )
        ans.append( (-b - sqrt(delta)) / (2*a) )
    elif delta < 0:
        solution = 0
    
    print(f"Get {solution} solution(s) in real number field.")
    i = 0
    for x in ans:
        i += 1
        print(f"x{i} = {x}")

    exit(0)