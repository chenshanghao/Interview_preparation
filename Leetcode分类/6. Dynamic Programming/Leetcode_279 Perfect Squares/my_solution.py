class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        output = [float('inf')] * (n+1)
        output[0] = 0
        output[1] = 1
        
        
        for i in range(2, n+1):
            j = 1
            while(j*j <= i):
                output[i] = min(output[i], output[i-j*j]+1)
                j += 1
        return output[n]  