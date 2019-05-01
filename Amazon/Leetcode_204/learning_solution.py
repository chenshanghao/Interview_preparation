class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        if n < 3: return 0
        
        is_prime = [True for _ in range(n)]
        is_prime[0] = is_prime[1] = False
        is_prime[2] = True
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        return sum(is_prime)
        