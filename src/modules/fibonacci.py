def fibonacci(n):
    """Fibonacci数のリストを返す

    e.g.
    import module_sample
    fibo = module_sample.fibo
    fibo(100)

    ---

    $ python fibonacci.py num
    """
    array = []
    a, b = 0, 1
    while a < n:
        array.append(a)
        a, b = b, a + b
    return array


if __name__ == "__main__":
    import sys

    print("exec as script")
    print(fibonacci(int(sys.argv[1])))
