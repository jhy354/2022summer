#!/usr/bin/env python3

from pandas import DataFrame, read_excel, set_option

def div_line() -> None:
    print('-' * 15)
    return


def init_df(show_all_data : bool = True, align_data : bool = True) -> None: 
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
    div_line()

    # (4)
    print(df1["文具"])
    print(df1["数量"])
    """
    df1 = df1.drop("数量", axis=1)
    df1.insert(1, "数量", ["17", "95", "89", "29"])
    """
    replaceList = ["17", "95", "89", "29"]
    for i in df1.index:
        df1.at[int(i), "数量"] = replaceList[int(i)]
    print(df1)
    div_line()
    

    # (5)
    # type(df1["数量"]) == <class 'pandas.core.series.Series'>
    s = df1["数量"]
    for i in s.index:
        if int(s[i]) > 30:
            print(df1.iloc[ [int(i)] ])
            
    print(df1.at[2, "文具"])
    div_line()

    # (6)
    print(1)
    addDf = DataFrame({
            "采集场所":["游泳馆"],
            "志愿者":["P"],
            "账号":["0163893"],
            "密码":["XXXX"],
            "采集人数":[200],
            "封包时间":["12:20:46"]
        },
        columns=[
            "采集场所", "志愿者", "账号",
            "密码", "采集人数", "封包时间"
        ]
    )
    # print(tmpdf)
    df = df.append(addDf, ignore_index=True)
    print(df)

    df = df.drop("密码", axis=1)
    print(df)
    df = df.drop(0, axis=0)
    print(df)
    div_line()

    # (7)
    tmpDf = df.drop(["志愿者", "账号", "封包时间"], axis=1)
    
    # 会warning
    # 去掉后如果类型不统一可能error
    for i in tmpDf["采集人数"].index:
        # print(type(tmpDf["采集人数"][i]))
        tmpDf["采集人数"][i] = int(tmpDf["采集人数"][i])
    
    g = tmpDf.groupby("采集场所", as_index=False)
    print(g.mean(0))

    # (8)
    df.sort_values(by="采集人数", ascending=False)
    print(df)

    exit(0)