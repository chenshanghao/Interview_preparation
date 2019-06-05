class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """
    def getAns(self, s, k):
        # Write your code here
        res = 0
        if not s:
            return res
        markStr = s[0]
        num = 1
        for i in range(1, len(s)):
            if num == k:
                res += 1
                num = 1
                markStr = s[i]
            else:
                if s[i] == markStr:
                    num += 1
                    continue
                else:
                    res += 1
                    num = 1
                    markStr = s[i]
                    
        if num >= 1:
            res += 1
            
                
        return res