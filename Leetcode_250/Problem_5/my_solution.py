class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        if not s:
            return ans
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        max_len = 1
        
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = True
                max_len = True
                ans = s[i:i+2] 
                
        for j in range(1,n):
            for i in range(0, j-1):
                if s[j] == s[i] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        ans = s[i:j+1]
        return ans