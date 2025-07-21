



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    c = a + b
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c

def knapsack01(target, arr):
    # given a target value and an array of tokens with different values,
    # can you make the target with the values in the arr?
    if target == 0:
        pass










