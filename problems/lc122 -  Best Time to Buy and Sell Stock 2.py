

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
        print("price: " + str(p), "min: " + str(minimum), "max: " + str(maximum), "profit: " + str(maximum - minimum))
    return profit


def multiMaxProfit(prices: [int]):
    if prices.__len__() == 0:
        return 0

    profit = 0
    diff = []

    for i in range(0, len(prices) - 1):
        d = prices[i+1] - prices[i]
        if d > 0: profit += d
        # diff.append(prices[i+1] - prices[i])
    # for k in diff:
    #     if k > 0: profit += k
    return profit




multiMaxProfit([2,4,1])       #2
multiMaxProfit([7,1,5,3,6,4]) #7
multiMaxProfit([7,6,4,3,1])   #0
multiMaxProfit([1,2,3,4,5])   #4










