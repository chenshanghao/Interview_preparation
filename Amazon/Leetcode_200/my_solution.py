class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        res = 0
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 1
                    self.helper(grid, i, j)
        return res
    
    def helper(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or not grid[i][j]:
            return
        grid[i][j] = 0
        self.helper(grid, i - 1, j)
        self.helper(grid, i + 1, j)
        self.helper(grid, i, j - 1)
        self.helper(grid, i, j + 1)
        
        
        
        
