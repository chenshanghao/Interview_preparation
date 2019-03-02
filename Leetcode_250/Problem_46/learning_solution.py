class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        self.res = []
        self.helper(nums, [])
        return self.res
    
    def helper(self, nums, temp):
        if len(temp) == len(nums):
            self.res.append(temp[:])
            
        for i in nums:
            if i not in temp:
                temp.append(i)
                self.helper(nums,temp)
                temp.pop()
    