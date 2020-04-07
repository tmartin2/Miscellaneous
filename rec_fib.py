'''
My implementation of the fibonacci algorithm
using recursion
'''

__author__ = "Trevor Martin"

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2) 

print(fibonacci(4))
print(fibonacci(6))
