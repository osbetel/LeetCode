
import math, timeit
# primeNumArray(int length) {
#         int[] primeArray = new int[length];
#         int index = 0;
#
#         do {
#             for (int k = 2; index < length; k++) {
#
#                 if (isPrime(k)) {
#                     primeArray[index] = k;
#                     index +=1;
#                 }
#             }
#         } while (index < length);
#         return primeArray;
#     }

def answer(n):
    ps = primeString(10000)  # +20 just in case
    ps = ps[0:10000]
    # print(len(ps))
    return ps[n:n+5]

def primeString(charLength):
    ps = ""
    for x in primeArray(20000):
        if len(ps) < charLength: ps += str(x)
    # print(len(ps))
    return ps

# returns boolean if x is prime
def isPrime(x):
    for i in reversed(xrange(2, x / 2 + 1)):
        if x % i == 0:
            return False
    return True


def primeArray(num):
    pa = []
    for k in range(2, num):
        if isPrime(k):
            pa.append(k)
    return pa

def primeArray2(num):
    # let 1 == true and 0 == false for prime values
    pa = [1] * (num / 2) # array of num size
    for i in range(1, int(num ** 0.5)):
        if pa[i] == 1:
            skip = 2 * i + 1
            # print(pa[i + skip: : skip])
            pa[i + skip: : skip] = [0] * ((num / 2 - 1 - i) / skip)
            # print([0] * ((num / 2 - 1 - i) / skip))
    # pa is now an array of num size with the "slots" for primes marked with a 1
    result = []
    for i in range(0, len(pa)):
        if pa[i] == 1: result.append(i * 2 + 1)
    # return [2] + [(x * 2 + 1) for x, y in enumerate(pa) if x and y > 0]
    result[0] = 2
    return result



def primeArrayEratos(num):
    pae = [1] * (num / 2)
    for k in range(1, int(math.sqrt(num))):
        if pae[k]:
            v = (2 * k + 1)
            # print(str(k) + " : " + str(v))
            pae[k + v: : v] = [0] * ((num / 2 - 1 - k) / v)
        # print(pa)
    # print(k)
    # via sieve of eratosthenes algorithm
    pae = [2] + [(k * 2 + 1) for k, j in enumerate(pae) if k and j > 0]
    return pae


def timefx(fx, n):
    start = timeit.default_timer()
    fx(n)
    end = timeit.default_timer()
    print(end - start)

def testall():
    timefx(primeArray, 10000)
    timefx(primeArrayEratos, 10000)
    timefx(primeArray2, 10000)

    p1 = primeArrayEratos(10000)
    p2 = primeArray(10000)
    p3 = primeArray2(10000)
    print(p1 == p2 == p3)

testall()

