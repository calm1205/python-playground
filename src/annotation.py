def f(name: str, age: int) -> None:
    """アノテーション

    引数や戻り値に型を指定することができる。
    型は実行時にはチェックされないが、IDEやlinterがチェックしてくれる。
    """
    print(f.__annotations__)
    print(name, age)


f("Alice", 20)
