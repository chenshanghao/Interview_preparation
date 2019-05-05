class Solution:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeatedSubstringPattern(self, s):
        # write your code here
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                subString = s[0:i]
                if subString * (n // i) == s:
                    return True
        return False