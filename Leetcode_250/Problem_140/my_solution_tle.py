class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        if not s:
            return res 
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        dict_index_str = {}
        for i in range(1, n+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict:
                    if not dp[i]:
                        dict_index_str[i] = []
                        dp[i] = True
                    if j==0:
                        dict_index_str[i].append(s[0:i])
                    else:
                        for str in dict_index_str[j]:
                            dict_index_str[i].append(str + " " + s[j:i])
        if n in dict_index_str:
            return dict_index_str[n]
        else:
            return res
                            
                    
                