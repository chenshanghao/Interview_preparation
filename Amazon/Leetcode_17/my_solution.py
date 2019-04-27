class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        res = []
        if not digits:
            return res
        dict_num_str = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }
        self.helper('', res, digits, 0, dict_num_str)
        return res
        
    
    def helper(self, tmp, res, digits, poiter, dict_num_str):
        if len(tmp) == len(digits):
            res.append(tmp[:])
            return
        string = dict_num_str[int(digits[poiter])]
        for s in string:
            new_tmp = tmp[:] + s
            self.helper(new_tmp, res, digits, poiter+1, dict_num_str)
        
        
