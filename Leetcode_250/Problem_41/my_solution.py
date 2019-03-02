class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        val_dict ={}
        for i in range(n):
            val_dict[nums[i]] = True
        
        for i in range(1,n+1):
            if i not in val_dict:
                return i
        return n+1