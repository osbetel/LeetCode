


# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# Maximum profit for a single trade of buying.
def maxProfit(prices: [int]):
    # we can simply assume the price is never less than 0
    if prices.__len__() == 0:
        return 0

    minimum = prices[0]
    maximum = prices[0]
    profit = 0
    for p in prices:
        if p < minimum:
            minimum = p
            maximum = p
        if p > maximum:
            maximum = p
        profit = max(profit, maximum - minimum)
        # print(p, minimum, maximum, maximum - minimum)
    return profit

maxProfit([2,4,1])       #2
maxProfit([7,1,5,3,6,4]) #5
maxProfit([7,6,4,3,1])   #0

