class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        # Write your code here
        if not A or not B:
            return -1
        if len(A) != len(B):
            return -1
        res = 0
        for i in range(len(A)):
            res += A[i] * B[i]
        return res
