class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """
    def isThreeDisctFactors(self, n):
        # write your code here
        fac = long(math.sqrt(n))
        if fac * fac != n:
            return False
        
        facRoot = long(math.sqrt(fac))
        for i in range(2, facRoot + 1):
            if fac % i == 0:
                return False
        return True
        