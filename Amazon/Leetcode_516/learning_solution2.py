class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
        n = len(s)
        dp0 = [0] * n
        dp1 = [1] * n
        dp2 = [0] * n
        for l in range(2, n + 1):
          for i in range(0, n - l + 1):        
            j = i + l - 1
            if s[i] == s[j]:
              dp0[i] = dp2[i + 1] + 2
            else:
              dp0[i] = max(dp1[i + 1], dp1[i])      
          dp0, dp1, dp2 = dp2, dp0, dp1
        return dp1[0]
        