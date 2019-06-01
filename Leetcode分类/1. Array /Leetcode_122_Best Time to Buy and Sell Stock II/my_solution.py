class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        res = 0
        if n < 2:
            return res
        minVal = prices[0]
        for i in range(1, n):
            if prices[i] <= minVal:
                minVal = prices[i]
            else:
                res += prices[i] - minVal
                minVal = prices[i]
        return res
        