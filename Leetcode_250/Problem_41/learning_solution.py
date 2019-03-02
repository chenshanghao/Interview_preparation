class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        i=0
        while i<n:
            current = nums[i]
            if current<=0 or current>n or nums[current-1] == current:
                i += 1
            else:
                nums[current -1], nums[i] = nums[i], nums[current-1]
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1