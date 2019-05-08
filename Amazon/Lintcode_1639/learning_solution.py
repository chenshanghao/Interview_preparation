class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        n = len(stringIn)
        charSet = set()
        result = set()
        j = 0
        for i in range(n):
            while j < n and len(charSet) < K:
                if stringIn[j] in charSet:
                    break
                
                charSet.add(stringIn[j])
                j += 1
                if len(charSet) == K:
                    result.add(stringIn[i:j])
                    
            charSet.remove(stringIn[i])
            
        return len(result)