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
