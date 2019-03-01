class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(result, sorted(candidates), target, 0, [])
        return result
    
    def helper(self, result, candidates, target, start, tmp):
        if sum(tmp) == target:
            result.append(tmp[:])
            return
        if sum(tmp) > target:
            return
        
        for i in range(start, len(candidates)):
            if i>start and candidates[i] == candidates[i-1]:
                continue
            tmp.append(candidates[i])
            self.helper(result, candidates, target, i+1, tmp)
            tmp.pop()