class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        
        # central symmetry 中心对称
        # axial symmetry 轴对称
        res = ''
        for i in range(len(s)):
            temp = self.findLongestPalindrome(s, i, i)
            if len(res) < len(temp):
                res = temp
            
            temp = self.findLongestPalindrome(s, i, i+1)
            if len(res) < len(temp):
                res = temp
        return res
            
        
        
    def findLongestPalindrome(self, s, l, r):
        len_s = len(s)
        while l >= 0 and r < len_s:
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l+1:r]