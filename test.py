import math


def weight_score(nums: [float]) -> float:
    print("source: ", a)

    k = len(nums)
    k =  int(k ** 0.5)

    # take k highest scores
    l = sorted(nums, reverse=True)
    c = l[:k]
    r = rms(c)
    return r

def rms(nums):
    squared = []
    print(f"worst {len(nums)} scores: ", nums)
    for x in nums:
        squared.append(x ** 1)
    s = sum(squared) / len(squared)
    s =  math.sqrt(s)
    print("score: ", s)
    return s

import random
a = [round(100 / random.randint(110, 10000), 5) for x in range(100000)]
# weight_score(a)
rms([0.9,0.9,0.9,0.1])
