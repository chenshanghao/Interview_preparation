class Solution:
    """
    @param nums: An array of integers.
    @return: nothing
    """
    def arrayReplaceWithGreatestFromRight(self, nums):
        # Write your code here.
        n = len(nums)
        rightMaximum = nums[-1]
        nums[-1] = -1
        for i in range(n-2, -1, -1):
            tmp = nums[i]
            nums[i] = rightMaximum
            rightMaximum = max(tmp, rightMaximum)