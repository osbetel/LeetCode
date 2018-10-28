
def myPow(x, n):
    if n == 0: return 1
    # if 0 < x < 1:

    r = 1
    s = abs(n)
    while s > 0:
        if s&1 == 1: r *= x
        s >>= 1
        x *= x

    if n > 0: return r
    else: return 1 / r



print(myPow(2.0, 1024))
