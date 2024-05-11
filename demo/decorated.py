# from ucb import trace

def trace(fn):
    def traced(*args):
        print('Calling', fn, 'on', args)
        result = fn(*args)
        print('Returning', result)
        return result
    return traced

@trace
def square(x):
    return x * x

# equivalent to square = trace(square)

@trace
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total

# print(square(5))
print(sum_squares_up_to(5))