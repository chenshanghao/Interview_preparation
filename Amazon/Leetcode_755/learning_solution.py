class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i, a in enumerate(A):
            if abs( a - i) > 1:
                return False
        return True