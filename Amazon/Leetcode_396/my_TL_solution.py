class Solution:
    """
    @param A: an array
    @return: the maximum value of F(0), F(1), ..., F(n-1)
    """
    def maxRotateFunction(self, A):
        # Write your code here
        n = len(A)
        B = [i for i in range(n)]
        res = float('-inf')
        for i in range(n):
            tmp = 0 
            for j in range(i-n, i, 1):
                tmp += A[j] * B[j+n-i]
            res = max(tmp, res)
        if res == float('-inf'):
            return 0
        else:
            return res