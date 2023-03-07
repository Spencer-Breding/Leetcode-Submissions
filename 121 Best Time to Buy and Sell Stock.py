import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = math.inf
        sellPrice = 0
        profit = 0
        for i in range(len(prices)):
            if(prices[i]-buyPrice>profit):
                profit = prices[i]-buyPrice
            if(buyPrice>prices[i]):
                buyPrice = prices[i]
        return profit
