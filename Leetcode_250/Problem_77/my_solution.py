class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n+1)]
        self.helper(res, nums, k, 0, [])
        return res
        
    def helper(self, res, nums, k, start, tmp):
        if len(tmp) == k:
            res.append(tmp[:])
            return
        
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.helper(res, nums, k, i+1, tmp)
            tmp.pop()
        