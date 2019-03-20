class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        n = len(nums)
        if n <= 2:  return res
        for i in range(0, n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            target = 0 - nums[i]
            left = i + 1
            right = n - 1
            while(left < right):
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < n-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                    
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res
        
        