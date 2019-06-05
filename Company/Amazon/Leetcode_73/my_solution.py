class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        point_list = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    point_list.append([i, j])
                    
        for point in point_list:
            for j in range(n):
                matrix[point[0]][j] = 0
            for i in range(m):
                matrix[i][point[1]] = 0
