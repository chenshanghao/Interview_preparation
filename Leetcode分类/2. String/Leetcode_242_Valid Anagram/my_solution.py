class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict_s_num = {}
        n = len(s)
        for i in range(n):
            if s[i] in dict_s_num:
                dict_s_num[s[i]] += 1
            else:
                dict_s_num[s[i]] = 1
        
        for i in range(n):
            if t[i] in dict_s_num and dict_s_num[t[i]] > 0:
                dict_s_num[t[i]] -= 1
            else:
                return False
        return True