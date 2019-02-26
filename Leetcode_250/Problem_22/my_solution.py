class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if not n:
            return res
        self.helper(0, 0, n, '', res)
        return res
        
    def helper(self, left, right, n, temp, result):
        if left == right and left == n:
            result.append(temp[:])
            return
        
        if left < right:
            return
        
        if left == right:
            new_temp = temp[:] + '('
            self.helper(left+1, right, n, new_temp, result)
            
        if left > right:
            if left < n:
                new_temp = temp[:] + '('
                self.helper(left+1, right, n, new_temp, result)
            self.helper(left, right+1, n, temp[:]+')', result)
        