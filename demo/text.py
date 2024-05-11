from operator import floordiv, mod

def divide_exact(n, d):
    """
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

# quotient, remainder = divide_exact(2013, 10)
# print(quotient, remainder)


'''
$ python -m doctest text.py 
# if right, no output
# else output something
'''



'''
$ python -m doctest -v text.py 
Trying:
    q, r = divide_exact(2013, 10)
Expecting nothing
ok
Trying:
    q
Expecting:
    201
ok
Trying:
    r
Expecting:
    3
ok
1 items had no tests:
    text
1 items passed all tests:
   3 tests in text.divide_exact
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
'''