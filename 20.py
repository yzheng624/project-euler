print reduce(lambda x, y: int(x) + int(y), str(reduce(lambda x, y: x * y, range(1, 101))))
