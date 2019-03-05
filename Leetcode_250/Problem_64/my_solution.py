class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:  return 0
        n = len(grid[0])
        if n == 0:  return 0
        
        sum_grid = [[0 for j in range(n)] for i in range(m)]
        
        sum_grid[0][0] = grid[0][0]
        for i in range(1, m):
            sum_grid[i][0] = sum_grid[i-1][0] + grid[i][0]
            
        for j in range(1, n):
            sum_grid[0][j] = sum_grid[0][j-1] + grid[0][j] 
            
        for i in range(1,m):
            for j in range(1,n):
                sum_grid[i][j] = min(sum_grid[i-1][j], sum_grid[i][j-1]) + grid[i][j]
        
        return sum_grid[m-1][n-1]