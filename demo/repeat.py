def repeat(k):
    '''
    when called with an argument k, print each argument i for which i == k

    >>> repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    '''
    # initial called return false
    # then repeat is taken charge by detector
    return detector(lambda j: False)(k)

def detector(have_seen_i_before):
    def detect(i):
        if have_seen_i_before(i):
            print(i)
        # return detector with new function that checks if i == j or have_seen_i_before(j)
        # this is a recursive function
        new_have_seen_i_before = lambda j: j == i or have_seen_i_before(j)
        return detector(new_have_seen_i_before)
        # equivalent to return detector(lambda j: j == i or have_seen_i_before(j))
    return detect

# repeat is equal to detector(lambda j: False)(k)
print(repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1))

# eg.
# have_seen_i_before0 = lambda j: False
# have_seen_i_before1 = lambda j: j == 1 or have_seen_i_before0(j)
# have_seen_i_before2 = lambda j: j == 7 or have_seen_i_before1(j)