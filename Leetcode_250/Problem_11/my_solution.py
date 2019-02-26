# Variables i and j define the container under consideration. We initialize them to first and last line, 
# meaning the widest container. Variable water will keep track of the highest amount of water we managed so far. 
# We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. 
# Multiply them to get how much water this container can hold, and update water accordingly. Next remove the smaller one of the two lines from consideration, 
# as justified above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        max_container = 0
        while(l<r):
            max_container = max(max_container, min(height[l], height[r])*(r-l))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return max_container
        
        
        