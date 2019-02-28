class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        if not nums:
            return res
        
        for i in range(1, len(nums)):
            if nums[res]<nums[i]:
                res += 1
                nums[res] = nums[i]
        return res+1
            