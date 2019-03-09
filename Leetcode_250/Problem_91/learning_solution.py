class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:  return 0
        dp = [0 for i in range(n+1)]
        dp[n] = 1
        dp[n-1] = 1 if s[n-1] != '0' else 0
        
        for i in range(n-2, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1] + dp[i+2] if int(s[i:i+2]) <= 26 else dp[i+1]
        return dp[0]
        