'''
My implementation of the fibonacci algorithm
using recursion
'''

__author__ = "Trevor Martin"

def fibonacci(number):
    if number == 0 or number == 1:
        return number
    return fibonacci(number-1) + fibonacci(number - 2) 

if __name__ == '__main__':
    print(fibonacci(int(input("Find the n-th fibonacci number: "))))
