class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dictSecert, dictguess = {}, {}
        bullCount, cowCount = 0, 0
        for index, number in enumerate(secret):
            if secret[index] == guess[index]:
                bullCount += 1
            if number in dictSecert:
                dictSecert[number] += 1
            else:
                dictSecert[number] = 1
        
        for number in guess:
            if number in dictguess:
                dictguess[number] += 1
            else:
                dictguess[number] = 1
        
        for key, value in dictguess.items():
            if key in dictSecert:
                cowCount += min(value, dictSecert[key])
        cowCount -= bullCount
        return str(bullCount) + 'A' + str(cowCount) + 'B'
        