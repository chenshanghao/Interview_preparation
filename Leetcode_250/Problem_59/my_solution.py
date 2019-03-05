class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 1. 奇数，填充中心店
        # 2. 偶数
        
        res = [[0 for i in range(n)] for j in range(n)]
        left, right = 0, n-1
        top, bottom = 0 , n-1
        val = 1
        
        while(left<right):
            for i in range(left, right):
                res[top][i] = val
                val += 1
            
            for i in range(top, bottom):
                res[i][right] = val
                val += 1
            
            for i in range(right, left, -1):
                res[bottom][i] = val
                val += 1
            
            for i in range(bottom, top, -1):
                res[i][left] = val 
                val += 1
            
            left, right = left+1, right-1
            top, bottom = top+1, bottom-1
            
        if n%2 == 1:
            res[bottom][right] = val
        
        return res
        