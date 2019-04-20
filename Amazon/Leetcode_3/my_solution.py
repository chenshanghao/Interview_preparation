class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        res = 0
        if not s:
            return res
        dict_val_index = {}
        start = 0
        
        for index, val in enumerate(s):
            if val not in dict_val_index or dict_val_index[val] < start:
                dict_val_index[val] = index
                res = max(res, index-start+1)
            else:
                start = dict_val_index[val] + 1
                dict_val_index[val] = index
                
        return res