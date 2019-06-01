class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        dictNumVal = {}
        for num in nums:
            if num in dictNumVal:
                return True
            else:
                dictNumVal[num] = False
        return False    