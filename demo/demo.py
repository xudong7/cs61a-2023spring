def func(n):
    """
    
    >>> func(8)
    2
    2
    2
    >>> func(9)
    3
    3
    >>> func(10)
    2
    5
    >>> func(11)
    11
    >>> func(12)
    2
    2
    3
    >>> func(858)
    2
    3
    11
    13
    """
    while n > 1:
        k = smallest_num(n)
        n //= k
        print(k)


def smallest_num(n):
    k = 2
    while n % k != 0:
        k += 1
    return k

# func(858)