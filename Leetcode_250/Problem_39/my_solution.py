class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(sorted(candidates), target, 0, [], result)
        return result
    
    def helper(self, candidates, target, start, tmp, result):
        total = sum(tmp)
        if total == target:
            result.append(tmp[:])
            return
        
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            tmp.append(candidates[i])
            self.helper(candidates, target, i, tmp, result)
            tmp.pop()
        