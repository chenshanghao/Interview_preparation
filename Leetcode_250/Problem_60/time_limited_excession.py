class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1,n+1)]
        result = []
        self.helper(result, nums, 0, [], k)
        return "".join(result[k-1])
    
    def helper(self, result, nums, start, tmp, k):
        if len(result) == k:
            return
        
        if len(tmp) == len(nums):
            result.append(tmp[:])
            return
        
        for i in range(0, len(nums)):
            if nums[i] in tmp:  continue
            tmp.append(nums[i])
            self.helper(result, nums, i+1, tmp, k)
            tmp.pop()
        
        