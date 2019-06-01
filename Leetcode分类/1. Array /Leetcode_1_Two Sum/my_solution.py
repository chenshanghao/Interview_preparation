class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        dictNumCount = {}
        for index, num in enumerate(nums):
            if target - num in dictNumCount:
                return [dictNumCount[target - num], index]
            else:
                dictNumCount[num] = index