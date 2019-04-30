class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []
        nums = sorted(nums)
        self.helper(res, [], 0, nums)
        return res
        
    def helper(self, res, tmp, start, nums):
        res.append(tmp[:])
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.helper(res, tmp, i+1, nums)
            tmp.pop()