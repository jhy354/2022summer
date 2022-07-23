#!/usr/bin/env python3

if __name__ == "__main__":
    # 很显然，这种是正确的写法
    t=int(input('请输入用时（秒）：'))
    v=25*3600/t
    if v<=100:
            print('正常')
    else:
        print('平均车速',round(v, 1))
        print('超速')    # 错误程序将这行放在了if-else外面，所以无论if判断的结果，都会输出"超速"
    
    exit(0)