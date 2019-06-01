class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dictNum1Cnt = {}
        ans = []
        for num1 in nums1:
            if num1 in dictNum1Cnt:
                dictNum1Cnt[num1] += 1
            else:
                dictNum1Cnt[num1] = 1
                
        for num2 in nums2:
            if (num2 in dictNum1Cnt) and (dictNum1Cnt[num2]>0):
                ans.append(num2)
                dictNum1Cnt[num2] -= 1
        return ans        