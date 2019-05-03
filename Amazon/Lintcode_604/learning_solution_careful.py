class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        n = len(nums)
        res = []
        if n < k or k == 0:
            return res
        
        windowSum = 0  
        for i in range(k):
            windowSum += nums[i]
        res.append(windowSum)
        for j in range(k, n):
            windowSum = windowSum - nums[j - k] + nums[j]
            res.append(windowSum)
        
        return res
