def f(position1, position2, /, position_or_keyword=3, *, keyword1, keyword2):
    """特殊引数
    位置のみ指定の引数は / の左側
    位置またはキーワード指定の引数は / と * の間
    キーワードのみ指定の引数は * の右側
    """

    print("f: ", position1, position2, position_or_keyword, keyword1, keyword2)


f(1, 2, keyword1=4, keyword2=5)  # 1 2 3 4 5
f(1, 2, position_or_keyword=3, keyword1=4, keyword2=5)  # 1 2 3 4 5


def f2(*, keyword1, keyword2):
    """キーワードのみ指定の引数は * の右側"""
    print("f2: ", keyword1, keyword2)


f2(keyword1=1, keyword2=2)


def f3(*args, **keyword_args):
    """*args は可変長引数

    **keyword_args は可変長キーワード引数
    """

    for arg in args:
        print("f3 arg: " + arg)

    for key in keyword_args:
        print("f3 keyword_args: ", key, keyword_args[key])


f3("hello", "world", keyword1=1, keyword2=2)
