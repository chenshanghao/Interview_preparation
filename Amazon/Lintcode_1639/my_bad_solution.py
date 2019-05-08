class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        res = set()
        n = len(stringIn)
        for i in range(0, n - K + 1):
            if len(stringIn[i: i + K]) == len(set(stringIn[i: i + K])):
                res.add(stringIn[i: i + K])
        return len(res)