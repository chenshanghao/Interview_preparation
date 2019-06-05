class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        
        if len(prices) <= 1:
            return maxProfit
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > minPrice:
                maxProfit = max(maxProfit, prices[i] - minPrice)
            else:
                minPrice = prices[i]
        return maxProfit