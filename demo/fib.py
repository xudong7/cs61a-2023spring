def fib(n):
    # initialize prev 0th, curr 1th fibonacci num
    prev, curr = 1, 0
    k = 0
    while k < n:
        # after this line finish, true change happen
        # so in this line, after 'prev = curr', the later 'prev' still equal to '1'
        prev, curr = curr, prev + curr
        k = k + 1
    return curr

for i in range(10):
    ret = fib(i)
    print(ret)


