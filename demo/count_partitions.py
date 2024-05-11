def trace(f):
    def g(x, y):
        ret = f(x, y)
        print(f'Calling {f.__name__}({x}, {y}) -> {ret}')
        return ret
    return g

@trace
def count_partitions(n, m):
    # n must be a non-negative integer
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # m must be a positive integer
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(2, 4))