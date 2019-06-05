class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """
    def getAns(self, s, k):
        # Write your code here
        n = len(s)
        ans = 1
        cnt = 1;
        for i in range (1,n):
            if (s[i] == s[i-1] and cnt < k) :
                cnt += 1
            else :
                ans += 1
                cnt = 1
        return ans