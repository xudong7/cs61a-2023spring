def make_adder(n):
    """

    >>> a = make_adder(3)
    >>> a(2)
    5
    """
    def adder(k):
        return k + n
    return adder

ret = make_adder(2000)(13)
print(ret)
