class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        left_max = [0] * n
        right_max = [0] * n
        l_max, r_max = float('-inf'), float('-inf')
        
        for i in range(n-2,-1,-1):
            r_max = max(height[i+1], r_max)
            right_max[i] = r_max
            
        for i in range(1, n):
            l_max = max(height[i-1], l_max)
            left_max[i] = l_max
        
            
        res = 0
        for i in range(1, n-1):
            if height[i] < left_max[i] and height[i] < right_max[i]:
                res += (min(left_max[i], right_max[i]) -height[i])
        return res
        