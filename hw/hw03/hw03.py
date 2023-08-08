HW_SOURCE_FILE=__file__


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    def func_adder(g):
        "*** YOUR CODE HERE ***"
        h = lambda x: func(g(x)) # Mind the order
        return composer(h)
        # func = lambda x: func(g(x))
        # return composer(func)
        # Get the Recursion error?
    return func, func_adder


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    g_arr = [None]*(n+1) 
    # Create an empty list with the length of n
    # Also can be used: g_arr = []...g_arr.append(...)
    for i in range(1, n + 1):
        if i <= 3: g_arr[i] = i
        else: g_arr[i] = g_arr[i-1] + 2*g_arr[i-2] + 3*g_arr[i-3]
    
    return g_arr[n]





def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    all_but_last, last = n // 10, n % 10
    if all_but_last == 0:
        return 0
    if all_but_last % 10 == last or all_but_last % 10 == last - 1:
        miss = 0
    else:
        miss = last - all_but_last % 10 - 1
    return missing_digits(all_but_last) + miss

def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    max_coin = max_coin_func(total)
    def count_helper(n, max_coin):
        if n == 0:
            return 1
        if n < 0:
            return 0
        elif max_coin < 1:
            return 0
        else:
            # Somehow I calculate the max_coin again in here, which caused a RecursionError...It waste me so much time...[angry]
            return count_helper(n - max_coin, max_coin) + count_helper(n, max_coin/2)
    return count_helper(total, max_coin)

def max_coin_func(total):
    max_exp = 0
    for i in range(total + 1):
        if pow(2, i) > total:
            max_exp = i - 1
            break
    max_coin = pow(2, max_exp)
    return max_coin

    # def helper(n, m):
    #     if n == 0:
    #         return 1
    #     elif n < pow(2, m):
    #         return 0
    #     else:
    #         return helper(n, m + 1) + helper(n - pow(2, m), m)
    # return helper(total, 0)


# def count_change(amount):
#     """Return the number of ways to make change for amount.

#     >>> count_change(7)
#     6
#     >>> count_change(10)
#     14
#     >>> count_change(20)
#     60
#     >>> count_change(100)
#     9828
#     >>> from construct_check import check
#     >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
#     True
#     """
#     "*** YOUR CODE HERE ***"

#     def get_max_denomination_starts_from(denomination):
#         assert (denomination == 1 or (denomination != 0 and (denomination &
#         (denomination - 1) == 0)))
#         if denomination > amount:
#             return denomination // 2
#         return get_max_denomination_starts_from(denomination * 2)

#     def count_change_partition(total_amount, max_denomination):
#         if total_amount == 0:
#             return 1
#         if total_amount < 0:
#             return 0
#         if max_denomination == 0:
#             return 0
#         return count_change_partition(
#             total_amount - max_denomination,
#             max_denomination) + count_change_partition(total_amount,
#                                                        max_denomination // 2)

#     return count_change_partition(amount, get_max_denomination_starts_from(1))




def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
        return
    spare = 6 - start - end
    move_stack(n - 1, start, spare)
    print_move(start, end)
    move_stack(n - 1, spare, end)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # Write in def form first
    # def function(x, function):
    #     if x == 1:
    #         return 1
    #     else:
    #         return function(x - 1, function) * x
    # return lambda n: function(n, function)

        
    return lambda n : (lambda x, function : 1 if x == 1 else x * function(x - 1, function))(n, lambda x, function : 1 if x == 1 else x * function(x - 1, function))
