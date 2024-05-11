def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1
    
def square(x):
    return x * x

# def positive(x):
#     return max(0, square(x) - 100)

def inverse(f):
    return lambda y : search(lambda x : f(x) == y)

def is_4_squared(x):
    return square(4) == x

def is_sqrt_of_16(x):
    return square(x) == 16

# def sqrt(y):
#     def is_y_squared(x):
#         return square(x) == y
#     return search(is_y_squared)

def inverse(f):
    def inverse_of_f(y):
        def inverse_y(x):
            return f(x) == y
        return search(inverse_y)
    return inverse_of_f


# find the num that is square of 4
print(search(is_4_squared))

# find the num that is sqrt of 16
print(search(is_sqrt_of_16))

# generalize the func
# print(sqrt(25))

# use inverse to inverse the func 'square' to 'sqrt'
sqrt = inverse(square)
print(sqrt(16))



