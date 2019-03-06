class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(res, nums, 0, [])
        return res
    
    def helper(self, res, nums, start, tmp):
        res.append(tmp[:])
        
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.helper(res, nums, i+1, tmp)
            tmp.pop()
        