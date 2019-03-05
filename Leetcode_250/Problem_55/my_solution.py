class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        if not nums:
            return True
        max_step = 0
        n = len(nums)
        for index, value in enumerate(nums):
            if max_step < index:    break
            max_step = max(max_step, index + nums[index])
            if max_step >= n-1:
                return True
        return False