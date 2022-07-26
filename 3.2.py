#!/usr/bin/env python3

from pandas import DataFrame, read_excel, set_option


def div_line() -> None:
    print('-' * 15)
    return


def init_df(show_all_data : bool = True, align_data : bool = True) -> None: 
    '''
    自动对齐
    '''
    if show_all_data:
        set_option('display.max_columns', 1000)
        set_option('display.width', 1000)
        set_option('display.max_colwidth', 1000)

    if align_data:
        set_option('display.unicode.ambiguous_as_wide', True)
        set_option('display.unicode.east_asian_width', True)
    
    return


if __name__ == "__main__":
    init_df()

    # (1)
    dic = {
    "文具":["铅笔", "钢笔", "橡皮", "尺子"],
    "数量":["71", "59", "98", "92"]
    }
    df1 = DataFrame(dic, columns=["文具", "数量"])
    print(df1)
    div_line()

    # (2)
    df = read_excel("test.xlsx")
    print(df)
    div_line()

    # (3)
    for i in df1.index:
        print(i)
    for i in df1.columns:
        print(i)
    for i in df1.values:
        print(i)
    print(df1.T)

    # (4)
    

    exit(0)