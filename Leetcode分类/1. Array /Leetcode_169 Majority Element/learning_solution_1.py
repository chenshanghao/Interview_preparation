class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        numLength = len(nums)
        if numLength == 1:
            return nums[0]
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                if dic[num] > numLength // 2:
                    return num
            
                