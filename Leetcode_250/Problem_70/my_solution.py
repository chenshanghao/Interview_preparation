class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Question 1: would n be smaller than 1 ?
        # Question 2: would n be larger than maxint
        #               In Python 3, this question doesn't apply. The plain int type is unbounded.
        #               In python 2, sys.maxint
        ans = [0, 1, 2]
        for i in range(3, n+1, 1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[n]
        