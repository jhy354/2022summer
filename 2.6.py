#!/usr/bin/env python3
# P99字符画

from PIL import Image

serarr = [
    '@', '#', '$', '%',
    '&', '?', '*', 'o',
    '/', '{', '[', '(',
    '|', '!', '^', '~',
    '-', '_', ':', ';',
    ',', '.', '`', ' ',
]
count = len(serarr)


def to_text(image_file) -> str:
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
    zoom_ratio = float(input("Image Zoom Ratio?\n>"))

    image_file = Image.open(rf"{image_name}.jpg")
    # 原参数0.9, 0.5
    w = int(image_file.size[0]*0.9*zoom_ratio)
    h = int(image_file.size[1]*0.5*zoom_ratio)
    image_file = image_file.resize((w, h))

    f = open(r"ASCII_ART.txt", 'w')
    f.truncate(0)    # 清空文件
    f.write(to_text(image_file))
    f.close()

    exit(0)