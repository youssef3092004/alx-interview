#!/usr/bin/python3
""" 
    Minimum Operations
"""
def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve exactly n 'H' characters in a text file,
    starting with a single 'H'. The only operations allowed are 'Copy All' and 'Paste'.

    Args:
        n (int): The target number of 'H' characters. Must be a positive integer.

    Returns:
        int: The minimum number of operations required to reach exactly n 'H' characters.
             Returns 0 if n is less than or equal to 1, as no operations are needed.
    """
    if n <= 1:
        return 0

    operation = 0
    i = 2

    while n > 1:
        if n % i == 0:
            operation += i
            n //= i  # Use integer division here
        else:
            i += 1
    return operation
