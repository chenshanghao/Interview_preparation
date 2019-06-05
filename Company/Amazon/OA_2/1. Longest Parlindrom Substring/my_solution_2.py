class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s
        maxLen = 1
        res = s[0:1]
        for i in range(n):
            tmp = self.helper(s, i, i)
            if len(tmp) > maxLen:
                res = tmp
                maxLen = len(tmp)
                
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > maxLen:
                res = tmp
                maxLen = len(tmp)
        return res
            
    
    def helper(self, s, l, r):
        n = len(s)
        while(l >= 0 and r < n and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l + 1:r]
        
        