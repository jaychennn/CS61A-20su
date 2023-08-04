"""
Higher-order Function:
pass in a function as an argument 
"""
def repeat(f, x):
    while x != f(x):
        x = f(x)
        print(f"x = {x}, f(x) = {f(x)}")
    return x
def g(y):
    return (y + 5)//3
# Always return the same value
repeat(g, 9000)

"""
Nested Def Statement
 
"""
def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_three = make_adder(3)
add_three(4)

"""Self_reference"""
"""
Use a picture to explain maybe better, but anyway I'll write down the process:
First we call the print_sums function, then it print n out, then define a nested function next_sum and return it to print_sums. Now call the next_sum(3), which returns print_sums(4), then print out '4', and define a new function next_sum( Just the same name as before, but in different frames. Environment is the combination of different frames ), and return it, then excute next_sum(5), which return print_sums(4+5), and all ends. A lot of returns and frames I think I haven't mastered yet... 
"""
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)

def curry(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g
from operator import add
adder = curry(add)
add_five = adder(5)
add_five(3) 
'''This add_five function add 5 to 3'''

"""Now rewrite it with lambda function in one single line"""
def lambda_curry2(f):
    return lambda x: lambda y: f(x, y)
"""The significance is change a single-argument function to a multiple-argument function, with the nested function to handle the rest arguments"""

# import from lab02

"""Impressive usage of currying function"""

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def func(n):
        cnt = 0
        for i in range(1, n+1):
            if condition(n, i): cnt += 1
        return cnt
    return func

"""??? Confused function"""
def flip(flop):
    if flop>2:
        return None
    flip = lambda flip:3
    return flip

def flop(flip):
    return flop

flip, flop = flop, flip

flip(flop(1)(2))(3)

"""Decorator: track the footprint of the function"""

def trace(fn):
    def traced(x):
        print("Calling the function", fn, "with the argument", x)
        return fn(x)
    return traced

@trace
def square(x):
    return x * x
"""Every time we call the function square, return a message 'Calling...'"""
def sum_squared_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k+1
    return total
