class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        max_profit = 0
        for i in prices:
            if (i < l):
                l = i
            if (i - l > max_profit):
                max_profit = i - l
        return max_profit
