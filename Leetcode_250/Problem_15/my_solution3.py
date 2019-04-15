class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n < 3:
            return  res
        nums = sorted(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            j = i + 1
            k = n - 1
            while(j < k):
                if j > i+2:
                    while(nums[j] == nums[j-1] and j<k):
                        j += 1
                if k < n-1:
                    while(nums[k] == nums[k+1] and j < k):
                        k -= 1
                if j >= k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return res
        