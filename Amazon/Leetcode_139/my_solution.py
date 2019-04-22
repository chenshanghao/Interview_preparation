class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        n = len(s)
        if not n:
            return True
            
        word_set = set(dict)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for word in word_set:
                len_word = len(word)
                if (i - len_word) >= 0 and s[i-len_word:i] == word and dp[i-len_word]:
                    dp[i] = True
                    break
        return True if dp[n] else False
            
         
        