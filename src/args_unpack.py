def unpack_args():
    """配列のunpack"""

    print(list(range(0, 5)))

    args = [3, 6]
    print(list(range(*args)))


def unpack_dict_args():
    """辞書のunpack"""

    dict_args = {"keyword1": 1, "keyword2": 2}

    def f(*, keyword1, keyword2):
        print(keyword1, keyword2)

    f(**dict_args)


unpack_args()
unpack_dict_args()
