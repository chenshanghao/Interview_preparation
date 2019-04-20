class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return [0]
        
        res = [0, 1]
        
        for i in range(2, n+1):
            rever_res = res[::-1]
            rever_res = [pow(2, i-1) | val for val in rever_res]
            res = res + rever_res
        return res