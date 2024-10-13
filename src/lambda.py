pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


for i in range(10):
    print((lambda: i * 2)(), end=", ")
print()

members = ["Bob", "Tom", "Ken"]
print(list(map(lambda x: x.upper(), members)))
