def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

withdraw = make_withdraw(100)
withdraw(25)
withdraw(100)

def make_withdraw_list(balance):
    b = [balance] # list can be changed
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

withdraw = make_withdraw_list(100)
withdraw(25)
withdraw(100)


def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g

def test1():
    a = f(1)
    b = a(2) 
    # same reference, every time call b, x will plus 1
    total = b(3) + b(4)
    print('total: ', total)

def test2():
    a = f(1)
    b = a(2)
    total = 10 + b(4)
    print('total: ', total)

test1()
test2()