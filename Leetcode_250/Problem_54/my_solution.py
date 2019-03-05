class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        
        left, top = 0, 0
        right, bottom = len(matrix[0]) - 1, len(matrix) - 1
        
        while left<right and top<bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
                
            for i in range(top, bottom):
                res.append(matrix[i][right])
                
            for i in range(right, left, - 1):
                res.append(matrix[bottom][i])
                
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
                
            left, top = left+1, top+1
            right, bottom = right-1, bottom-1
        
        if left == right and top == bottom:
            res.append(matrix[top][left])
        elif left == right:   # top to bottom val
            for i in range(top, bottom+1):
                res.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        return res
            