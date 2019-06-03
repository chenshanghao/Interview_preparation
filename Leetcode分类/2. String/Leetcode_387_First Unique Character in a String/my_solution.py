class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictCharNum ={}
        n = len(s)
        for i in range(n):
            if s[i] in dictCharNum:
                dictCharNum[s[i]] += 1
            else:
                dictCharNum[s[i]] = 1
        for i in range(n):
            if dictCharNum[s[i]] == 1:
                return i
        return -1