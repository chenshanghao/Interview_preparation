class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid:    return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(m, n, i, j, grid)
        return res
    
    def helper(self, m, n, i, j, grid):
        if i<0 or j<0 or i==m or j==n or grid[i][j]!='1':  return
        
        grid[i][j] = '#'
        self.helper(m, n, i-1, j, grid)
        self.helper(m, n, i+1, j, grid)
        self.helper(m, n, i, j-1, grid)
        self.helper(m, n, i, j+1, grid)
        return
        
        