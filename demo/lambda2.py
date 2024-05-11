# test1
def func(f, g):
    def compose(x):
        return f(g(x))
    return compose
    # another method
    # return lambda x : f(g(x))

def square(x):
    return x * x

def add_one(x):
    return x + 1

h = func(square, add_one)
# another method
# h = func(lambda x : x * x, lambda y : y + 1)
result = h(12)

print(result)

# test2
def f(x):
    return x + 1

g = lambda y = 1 : f

eight = g()(5)


print(eight)