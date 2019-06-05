class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        len_prices = len(prices)
        res = 0
        
        # if the length of prices is smaller than 2, return res = 0
        if len_prices < 2:
            return res
            
        # for-loop update the lowest prices and check the Maximum profit
        min_val = prices[0]
        for i in range(1, len_prices):
            if prices[i] < min_val:
                min_val = prices[i]
            else:
                res = max(res, prices[i] - min_val)
        return res
