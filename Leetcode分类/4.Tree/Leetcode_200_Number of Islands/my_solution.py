class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(m, n, i, j, grid)
        return res
    
    def helper(self, m, n, i, j, grid):
        if i<0 or j<0 or i==m or j==n:
            return
        if grid[i][j] == '1':
            grid[i][j] = '#'
            self.helper(m, n, i-1, j, grid)
            self.helper(m, n, i+1, j, grid)
            self.helper(m, n, i, j-1, grid)
            self.helper(m, n, i, j+1, grid)