class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:  return 0
        
        last_sum = float('-inf')
        max_sum = float('-inf')

        for i in range(0, n):
            last_sum = max(last_sum + nums[i], nums[i])
            max_sum = max(last_sum, max_sum)
        
        return max_sum
        