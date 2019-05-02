class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        listS = [0] * 256
        listT = [0] * 256
        for i in s:
            listS[ord(i)] += 1
        for j in t:
            listT[ord(j)] += 1
            
        for i in range(256):
            if listS[i] != listT[i]:
                
                return False
        return True
