def remove_1(n, digit):
    """Return all digits of n that are not DIGIT, for DIGIT in the range of 10.

    >>> remove(243132, 3)
    2412
    >>> remove(243132, 2)
    4313
    >>> remove(243132, 1)
    2432
    >>> remove(243132, 4)
    23132
    >>> remove(243132, 5)
    243132
    """
    kept, num = 0, 0
    # remove the digit
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            # why 10 ** num? 
            # because we need to keep the digit in the right place
            kept = kept + last * (10 ** num)
            num = num + 1
    return kept

def remove_2(n, digit):
    """Return all digits of n that are not DIGIT, for DIGIT in the range of 10.

    >>> remove(243132, 3)
    2412
    >>> remove(243132, 2)
    4313
    >>> remove(243132, 1)
    2432
    >>> remove(243132, 4)
    23132
    >>> remove(243132, 5)
    243132
    """
    kept, num = 0, 0
    # remove the digit
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept / 10 + last
            num = num + 1
    return round(kept * 10 ** (num - 1))

print(remove_1(243132, 3))
print(remove_2(243132, 3))