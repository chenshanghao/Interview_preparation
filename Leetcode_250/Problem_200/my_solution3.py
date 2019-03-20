class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return res
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(i, j, m, n, grid, res)
        return res
    
    def helper(self, i, j, m, n, grid, res):
        if i<0 or j<0 or i==m or j==n:
            return
        if grid[i][j] == '1':
            grid[i][j] = '#'
            self.helper(i-1, j, m, n, grid, res)
            self.helper(i+1, j, m, n, grid, res)
            self.helper(i, j-1, m, n, grid, res)
            self.helper(i, j+1, m, n, grid, res)
            