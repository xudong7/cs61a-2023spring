def computation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(k):
    return k

def cube(k):
    return k * k * k

def compute_identity(n):
    """
    >>> compute_identity(5)
    15
    """
    return computation(n, identity)

def compute_cube(n):
    """
    >>> compute_cube(5)
    225
    """
    return computation(n, cube)

# print(compute_identity(5))
# print(compute_cube(5))



