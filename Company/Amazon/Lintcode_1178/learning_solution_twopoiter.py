class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
        n = len(nums)
        nums.sort()
        result = set([])
        left, right = 0, 1
        while right <= n - 1:
            while left < right and nums[right] - nums[left] >= k:
                if nums[right] - nums[left] == k:
                    result.add((nums[left], nums[right]))
                left += 1
            right += 1
        return len(result)