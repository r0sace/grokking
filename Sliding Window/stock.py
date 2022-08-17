def max_profit(prices):
    left = 0
    profit = 0

    for right in range(1, len(prices)):
        if prices[right] < prices[left]:
            left = right
        else:
            profit = max(profit, prices[right] - prices[left])

    return profit

max_profit([7,1,5,3,6,4])