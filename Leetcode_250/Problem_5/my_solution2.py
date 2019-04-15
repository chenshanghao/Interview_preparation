class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        if not s:
            return res
        res = s[0]
        max_len = 1
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

            
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                res = s[i:i+2]
        
        for i in range(2, n):
            for j in range(0, i):
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        res = s[j:i+1]
        return res
                
                
        