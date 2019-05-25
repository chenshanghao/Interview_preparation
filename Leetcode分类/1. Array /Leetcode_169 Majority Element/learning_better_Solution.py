class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        return cand
            
                