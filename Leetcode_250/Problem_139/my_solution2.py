class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(1, n+1):
            for word in wordDict:
                m = len(word)
                if i-m >= 0 and word == s[i-m:i] and dp[i-m]:
                    dp[i] = True
        return dp[n]
        