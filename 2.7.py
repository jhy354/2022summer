#!/usr/bin/env python3

if __name__ == "__main__":
    f = open("gushi.txt", 'r')
    text = ''
    for line in f.readlines():
        text += line.strip()
    
    
    arr = ''
    i = 0
    for char in text:
        if i >= 5:
            break
        arr += char
        i += 1
    print(arr)
    f.close()

    f = open("gushi.txt", 'r')
    print(f.readline())
    f.close()

    print(text)

    f = open("test.txt", 'w')
    f.write("123\n")
    f.write("456\n")
    f.close()

    exit(0)