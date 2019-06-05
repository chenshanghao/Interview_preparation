class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n <= 1:
            return 0
        left_max = [0] * n
        right_max = [0] * n
        l_max, r_max = 0, 0
        
        for i in range(n-2,-1,-1):
            r_max = max(heights[i+1], r_max)
            right_max[i] = r_max
            
        for i in range(1, n):
            l_max = max(heights[i-1], l_max)
            left_max[i] = l_max
        
            
        res = 0
        for i in range(1, n-1):
            if heights[i] < left_max[i] and heights[i] < right_max[i]:
                res += (min(left_max[i], right_max[i]) - heights[i])
        return res
        
        