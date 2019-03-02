class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []
        
        if not n:
            return result
        
        visited = [False] * n
        self.helper(sorted(nums), visited, [], result)
        return result
    
    def helper(self, nums, visited, tmp, result):
        if len(tmp) == len(nums): 
            result.append(tmp[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:  continue
            if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            tmp.append(nums[i])
            visited[i] = True
            self.helper(nums, visited, tmp, result)
            tmp.pop()
            visited[i] = False