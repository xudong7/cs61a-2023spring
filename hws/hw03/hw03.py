HW_SOURCE_FILE = __file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    # "*** YOUR CODE HERE ***"
    # another approach:
    # cnt = 0
    # while n > 0:
    #     n, k = n // 10, n % 10
    #     cnt = cnt + 1 if k == 8 else cnt
    # return cnt 
    if n == 0:
        return 0
    elif n % 10 == 8:
        return 1 + num_eights(n // 10)
    else:
        return num_eights(n // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    # "*** YOUR CODE HERE ***"
    # k is the current index, p is the current value, up is the direction
    def helper(k, p, up):
        if k == n:
            return p
        # if k is a multiple of 8 or contains 8, then change the direction
        if k % 8 == 0 or num_eights(k) > 0:
            return helper(k + 1, p - up, -up)
        return helper(k + 1, p + up, up)
    return helper(1, 1, 1)
    

def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # "*** YOUR CODE HERE ***"
    # def func(n, coin):
    #     if n == 0:
    #         return 1
    #     if n < 0 or coin == None:
    #         return 0
    #     # Use the current coin or not
    #     with_coin = func(n - coin, coin)
    #     # Use the next smaller coin
    #     without_coin = func(n, next_smaller_coin(coin))
    #     return with_coin + without_coin
    # return func(change, 25)
    def func(n, coin):
        if n == 0:
            return 1
        if n < 0 or coin == None:
            return 0
        with_this_coin = func(n - coin, coin)
        without_this_coin = func(n, next_larger_coin(coin))
        return with_this_coin + without_this_coin
    return func(change, 1)

