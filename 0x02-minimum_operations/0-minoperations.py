#!/usr/bin/python3
def minOperations(n):
    operation = 0
    i = 2
    
    while n > 1:
        if n % i == 0:
            operation += i
            n /= i
        else:
            i += 1
    return operation
