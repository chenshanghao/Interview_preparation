class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                return True
            else:
                dict_nums[i] = False
        return False
        
        