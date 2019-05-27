class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numLength  = len(nums)
        m, countM = -1, 0
        n, countN = -1, 0
        for num in nums:
            if num == m:
                countM += 1
            elif num == n:
                countN += 1
            elif countM == 0:
                countM = 1
                m = num
            elif countN == 0:
                countN = 1
                n = num
            else:
                countM -= 1
                countN -= 1
        
        countM, countN = 0, 0
        for num in nums:
            if num == m:
                countM += 1
            if num == n:
                countN += 1
        res = []

        if countM > numLength / 3:
            res.append(m)
        if countN > numLength / 3:
            res.append(n)
        return res
        