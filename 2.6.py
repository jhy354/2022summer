#!/usr/bin/env python3
# P99字符画
# serarr? asd?变量名起得真奇怪(bushi

from PIL import Image
from os import system as shell
from platform import system

serarr = \
[
    '@', '#', '$', '%',
    '&', '?', '*', 'o',
    '/', '{', '[', '(',
    '|', '!', '^', '~',
    '-', '_', ':', ';',
    ',', '.', '`', ' '
]
count = len(serarr)


def to_text(image_file):
    asd = ''
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            r, g, b = image_file.getpixel((w, h))
            gray = int(r*0.299 + g*0.587 + b*0.114)
            asd += serarr[int( gray/(255/(count-1)) )]
        asd += '\r\n'    # \r回到当前行开头
    return asd


if __name__ == "__main__":
    image_name = input("Image Name?\n>")
    
    if system() == "Windows":
        shell_code = r"copy nul ASCII_ART.txt"    # 新建空白文件,cmd反人类操作
    elif system() == "Linux":
        shell_code = rf"touch ./ASCII_ART.txt"
    else:
        print("Please use it under Windows or Linux")
        exit(1)

    image_file = Image.open(rf"{image_name}.jpg")
    image_file = image_file.resize(( int(image_file.size[0]*0.5), int(image_file.size[1]*0.25) ))    # 原参数0.9, 0.5

    shell(shell_code)
    f = open(r"ASCII_ART.txt", 'a')
    f.truncate(0)    # 清空文件
    f.write(to_text(image_file))
    f.close()

    exit(0)