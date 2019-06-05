class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictStrNum = {}
        for character in s:
            if character in dictStrNum:
                dictStrNum[character] += 1
            else:
                dictStrNum[character] = 1
        print(dictStrNum)
        res = 0
        oddFlag = False
        for key,val in dictStrNum.items():
            if val % 2 == 0:
                res += val 
            else:
                res += val - 1
                oddFlag = True
        return res + 1 if oddFlag == True else res
        
        