class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        J = set(J)
        dictWordNum = {}
        res = 0
        for j in J:
            dictWordNum[j] = 1
        for s in S:
            if s in dictWordNum:
                res += 1
        return res
        