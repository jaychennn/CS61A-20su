# Some interesting built-in functions
"""
>>> max(range(2), key = lambda x: 7 - (x-4)*(x-2))
1
>>> max(range(3), key = lambda x: 7 - (x-4)*(x-2))
2
>>> max(range(4), key = lambda x: 7 - (x-4)*(x-2))
3
>>> max(range(5), key = lambda x: 7 - (x-4)*(x-2))
3
>>> max(range(6), key = lambda x: 7 - (x-4)*(x-2))

"""

# Tree
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)
# Label is the data stores in the root node, and the branches are like the next node in linked-list, which points to the next tree
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

"""
>>> fib_tree(0)
[0]
>>> fib_tree(1)
[1]
>>> fib_tree(2)
[1, [0], [1]]
>>> fib_tree(3)
[2, [1], [1, [0], [1]]]
>>> fib_tree(4)
[3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]
>>> fib_tree(5)
[5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
"""
"""
? Constructor
tree(label, branches=[]): creates a tree object with the given label value at its root node and list of branches. Notice that the second argument to this constructor, branches, is optional - if you want to make a tree with no branches, leave this argument empty.

? Selectors
label(tree): returns the value in the root node of tree.
branches(tree): returns the list of branches of the given tree.

? Convenience function
is_leaf(tree): returns True if tree's list of branches is empty, and False otherwise.
"""

def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    Hint: Consider how you can use the 0 or 1 returned by k%2 to alternatively access the beginning and the middle of the list.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    M = len(deck) // 2 
    return [deck[k//2 + M*(k % 2)] for k in range(len(deck))]