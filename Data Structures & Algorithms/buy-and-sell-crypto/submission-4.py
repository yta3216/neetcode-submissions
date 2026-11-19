class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        r = prices[0]
        max_profit = 0
        for i in prices:
            
            if (r < i):
                r = i
            if (i < l):
                l = i
                r = i
            if (r - l > max_profit):
                max_profit = r - l
        return max_profit
