class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        if not(pow(-2,31)< x < pow(2,31)-1):
            return res
        flag = 1 if x>=0 else -1
        x = abs(x)
        while x:
            tail = x % 10
            x = x//10 
            res = res * 10 + tail
        
        res = res * flag
        if not(pow(-2,31) < res < pow(2,31)-1):
            return 0
        else:
            return res