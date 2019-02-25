class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        dict_char_pos = {}
        
        for i in range(len(s)):
            if s[i] in dict_char_pos:
                if dict_char_pos[s[i]] >= start:
                    start = dict_char_pos[s[i]]+1
                    dict_char_pos[s[i]] = i
                else:
                    dict_char_pos[s[i]] = i
                    max_len = max(i-start+1, max_len)
            else:
                dict_char_pos[s[i]] = i
                max_len = max(i-start+1, max_len)
        return max_len
        