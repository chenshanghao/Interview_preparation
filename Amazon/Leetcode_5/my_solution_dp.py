class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        n = len(s)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        res = ''
        max_len = 1
        for i in range(n):
            dp[i][i] = 1
            res = s[i]
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res = s[i:i+2]
                max_len = 2
                
        for i in range(2,n):
            for j in range(i):
                if dp[j+1][i-1] and s[i] == s[j]:
                    dp[j][i] = i
                    if i-j+1 > max_len:
                        max_len = i-j+1
                        res = s[j:i+1]
        return res
            