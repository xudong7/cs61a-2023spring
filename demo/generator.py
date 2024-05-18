def func(start, end):
    while start < end:
        yield start # first stop here, then start from here
        start += 1

def a_then_b(a, b):
    yield from a 
    yield from b

def prefixes(x):
    if x:
        yield from prefixes(x[:-1])
        yield x

def substrings(x):
    if x:
        yield from prefixes(x)
        yield from substrings(x[1:])

def test1():
    start, end = 0, 5
    gen = func(start, end)
    for k in gen:
        print(k)

def test2():
    gen = list(a_then_b([0, 2, 6, 19], [1, 22, 3, 5]))
    print(gen)

def test3():
    for k in substrings('program'):
        print(k, end=' ')

test1()
test2()
test3()