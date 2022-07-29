#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ----------CONFIG---------- #
SAMPLE_SIZE = int(2*1e5)
TOTAL_LEN_OF_RANDOM = int(1e6)
# ----------CONFIG---------- #


from random import randint
import csv

# 10*5+5 = 55
# 复姓来五个意思意思算了
surname = [
    "李", "王", "张", "刘", "陈", "杨", "赵", "黄", "周", "吴",
    "徐", "孙", "胡", "朱", "高", "林", "何", "郭", "马", "罗",
    "梁", "宋", "郑", "谢", "韩", "唐", "冯", "于", "董", "萧",
    "程", "曹", "袁", "邓", "许", "傅", "沈", "曾", "彭", "吕",
    "苏", "卢", "蒋", "蔡", "贾", "丁", "魏", "薛", "叶", "阎",
    "欧阳", "太史", "端木", "上官", "司马"
]

# 10*5+5 = 55
surnameWeight = [
    7.9, 7.4, 7.0, 5.3, 4.5, 3.0, 2.2, 2.2, 2.1, 2.0,
    1.7, 1.5, 1.3, 1.2, 1.2, 1.1, 1.1, 1.1, 1.0, 0.8,
    0.8, 0.8, 0.7, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
    0.1, 0.1, 0.1, 0.3, 0.4
]

# 6*25 = 150
personalName = [
    "泽", "辰", "轩", "皓", "明", "杰",
    "凡", "一", "凡", "栋", "非", "浩",
    "昊", "乐", "杰", "鸿", "佳", "雨",
    "彬", "仁", "旭", "浩", "杰", "林",
    "诺", "康", "湃", "决", "颛", "丽",
    "筠", "博", "苑", "哲", "敏", "展",
    "圣", "烨", "晗", "愉", "宗", "宸", 
    "瑜", "瑾" ,"煜", "航", "锦", "曦",
    "海", "浪", "浩", "泽", "聪", "琳",
    "娜", "瑞", "晨", "鑫", "驿", "浩",
    "力", "明", "永", "健", "世", "广",
    "志", "义", "兴", "良", "海", "山",
    "仁", "丰", "波", "森", "波", "宁",
    "贵", "福", "生", "龙", "元", "全",
    "国", "胜", "学", "祥", "才", "佳",
    "强", "宁", "发", "武", "新", "利",
    "清", "飞", "彬", "富", "顺", "信",
    "子", "杰", "涛", "鹏", "宇", "衡",
    "昌", "成", "康", "星", "光", "天",
    "达", "安", "岩", "中", "茂", "进",
    "林", "厚", "庆", "磊", "有", "坚",
    "和", "彪", "博", "诚", "先", "敬",
    "震", "振", "壮", "会", "思", "功",
    "松", "善", "群", "豪", "心", "邦",
    "承", "乐", "绍", "民", "友", "裕",
    "河", "哲", "江", "超", "浩", "亮"
]


def get_tot_weight() -> float:
    tot = 0
    for i in surnameWeight:
        tot += i
    return tot


def get_insert_point(
    startPoint : int,
    weight : float,
    totWeight : float,
    totLen : int = int(1e5)
) -> int:
    '''
    根据起始位置, 按权重比和范围算出结束位置
    '''
    ratio = weight/totWeight
    secLen = ratio*totLen
    p = startPoint + secLen
    return p


def generate_name(
    surN : str,
    length : int = 3
) -> str:
    name = ""
    name += surN
    
    for i in range( length-len(surN) ):
        personalN = randint(0, len(personalName)-1)
        name += personalName[personalN]

    return name


if __name__ == "__main__":
    f = open("xm.csv", mode='w', encoding="utf-8-sig", newline='')
    writer = csv.writer(f)
    
    result = []
    tot = get_tot_weight()
    
    # 创建姓氏权重随机种子List
    surNSeed = []
    for i in range(SAMPLE_SIZE):
        surNSeed.append( randint(0, TOTAL_LEN_OF_RANDOM-1) )

    # 遍历姓氏List,匹配种子List
    prevInsertP = 0
    surnameIndex = 0
    for i in surname:
        insertP = get_insert_point(
            prevInsertP,
            surnameWeight[surnameIndex],
            tot,
            TOTAL_LEN_OF_RANDOM
        )
        for j in surNSeed:
            if prevInsertP <= j < insertP:
                result.append( [generate_name(i)] )
        surnameIndex += 1

    writer.writerows(result)

    exit(0)