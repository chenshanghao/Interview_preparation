class Solution:
    """
    @param matrix: a lists of integers
    @return: nothing
    """
    def rotate(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return matrix
        
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(m):
            matrix[i] = matrix[i][::-1]
        return matrix
