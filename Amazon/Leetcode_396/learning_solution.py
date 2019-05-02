# F(k) =   0 * Bk[0]   + 1 * Bk[1]   + ... + (n-1) * Bk[n-1]
# F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
#       =               0 * Bk[1]   + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
# Then  F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
#                     = (Bk[0] + ... + Bk[n-1]) - nBk[0]
#                     = sum - nBk[0]
# Thus, F(k) = F(k-1) + sum - nBk[0]
# F[i]=F[i−1]+sum−n∗a[n−i]

  
       

class Solution:
    """
    @param A: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """
    def maxRotateFunction(self, A):
        # Write your code here
        s = sum(A)
        curr = sum([i * a for i, a in enumerate(A)])
        maxVal = curr
        n = len(A)
        for i in range(1, n):
            curr = curr - n * A[n-i] + s
            maxVal = max(maxVal, curr)
        return maxVal