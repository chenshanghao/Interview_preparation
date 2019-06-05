# https://www.youtube.com/watch?v=-I8w2_sN93c

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return 
        firstRow, firstCol = False, False
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
                break
                
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
                break
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
        
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0