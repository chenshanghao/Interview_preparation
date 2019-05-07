class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        res = 0
        if not matrix or not matrix[0]:
            return res
        m, n = len(matrix), len(matrix[0])
        i, j = 0, len(matrix[0]) - 1
        while i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]):
            if matrix[i][j] == target:
                res += 1
                i += 1
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return res