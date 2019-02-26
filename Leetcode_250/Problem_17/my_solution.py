digit2letters = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        
        self.helper('', digits, res)
        return res
        
    def helper(self, tmp, digits, res):
        n = len(tmp)
        if n == len(digits):
            res.append(tmp[:])
            return
        
        for i in digit2letters[digits[n]]:
            new_tmp = tmp[:] + i
            self.helper(new_tmp, digits, res)
        