def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
    
"""
Mutual Recursion
Example: Luhn Algorithm---verify your credit card code
    sum up all the digits of the card number, with every second number doubled when sum, if that doubled number is bigger than 9, use the sum of its all digits
"""
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    # The 2 lines below implement the function of double the digits every second number
    all_but_last, last = split(n)
    luhn_digit = sum_digits(last * 2)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
        
"""cascade"""
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

"""
Inverse cascade
>>> inverse_cascade(1234)
1
12
123
1234
123
12
1
"""
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
    
"""
Counting Partitions: parts up n to the size m
>>> count_partitions(5, 3)
5
# 1+1+1+1+1 = 5
# 1+1+1+2 = 5
# 1+2+2 = 5
# 1+1+3 = 5
# 2+3 = 5
"""
def count_partitions(n, m):
    if n == 0: return 1
    elif n < 0: return 0
    elif m == 0: return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m
