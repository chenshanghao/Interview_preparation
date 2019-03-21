class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        wordDict = set(wordDict)
        dp[0] = True
        
        for j in range(1, n+1):
            for i in range(0, j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        
        return dp[n]