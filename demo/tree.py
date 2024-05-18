def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def tree(label, branches=[]):   
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts)

def leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        leaves_list = [leaves(b) for b in branches(t)]
        return sum(leaves_list, []) # merge all lists into one list

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        incremented_branches = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), incremented_branches)

def increment(t):
    # if is_leaf(t):
    #     return tree(label(t) + 1)
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t):
    print(label(t))
    for b in branches(t):
        print_tree(b)

def print_sum(t, so_far):
    so_far += so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sum(b, so_far)

def add_trees(t1, t2):
    '''
    add label of same index, if not have both, add one of label
    create a new tree and return it
    '''
    result_label = label(t1) + label(t2)
    result_branch = []
    i = 0
    while i < len(branches(t1)) and i < len(branches(t2)):
        b1, b2 = branches(t1)[i], branches(t2)[i]
        new_branch = add_trees(b1, b2)
        result_branch = result_branch + new_branch
        i = i + 1
    result_branch = result_branch + branches(t1)[i:]  
    result_branch = result_branch + branches(t2)[i:]  
    return tree(result_label, result_branch)
    # improved version
    result_label = label(t1) + label(t2)
    result_branch = [add_trees(b1, b2) 
                     for b1, b2 in 
                     zip(branches(t1), branches(t2))]
    i = len(result_branch)
    result_branch = result_branch + branches(t1)[i:]  
    result_branch = result_branch + branches(t2)[i:]  
    return tree(result_label, result_branch)
    # rec version
    def build_result_branch(bs1, bs2):
        if not bs1:
            return bs2
        if not bs2:
            return bs1
        f = add_trees(bs1[0], bs2[0])
        return [f] + build_result_branch(bs1[1:], bs2[1:])
    result_label = label(t1) + label(t2)
    result_branch = build_result_branch(branches(t1), branches(t2))
    return tree(result_label, result_branch)

def tree_test():
    '''
    tree data structure
    '''
    tree_1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
    # tree_1 = tree(3, [2])
    print(tree_1)
    # fib_tree
    print(fib_tree(5))
    print(count_leaves(fib_tree(5)))
    # count_leaves(fib_tree(n)) = fib(n+1)

    print(leaves(fib_tree(5)))
    print(increment_leaves(fib_tree(5)))
    print(increment(fib_tree(5)))
    print_tree(fib_tree(5))
    print_sum(fib_tree(5), 0)

def sum_test():
    print(sum([3, 4, 5]))
    print(sum([[3], [1, 6]], start=[]))

if __name__ == '__main__':
    tree_test()
    sum_test()



