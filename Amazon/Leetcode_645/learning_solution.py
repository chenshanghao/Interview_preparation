class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sall = sum(list(range(1, len(nums)+1)))
        sset = sum(set(nums))
        snum = sum(nums)

        miss    = sall - sset
        repeat  = snum - sset

        return [repeat, miss]