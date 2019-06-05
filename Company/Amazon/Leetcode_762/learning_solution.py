class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        primeList = [2,3,5,7,11,13,17,19]
        res = 0
        for i in range(L, R+1):
            if bin(i).count('1') in primeList:
                res += 1
        return res
                