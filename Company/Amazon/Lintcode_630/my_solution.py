class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        stack = [(0, 0)]
        res = 0
        
        while stack:
            new_stack = []
            res += 1
            for coord in stack:
                # case 1:
                x, y = coord[0] + 2, coord[1] + 1
                if x < m and y < n and not grid[x][y] and not dp[x][y]:
                    if x == m - 1 and y == n - 1:
                        return res
                    else:
                        dp[x][y] = 1
                        new_stack.append((x, y))
                # case 2:
                x, y = coord[0] + 1, coord[1] + 2
                if x < m and y < n and not grid[x][y] and not dp[x][y]:
                    if x == m - 1 and y == n - 1:
                        return res
                    else:
                        dp[x][y] = 1
                        new_stack.append((x, y))
                # case 3:
                x, y = coord[0] - 1, coord[1] + 2
                if x >= 0 and y < n and not grid[x][y] and not dp[x][y]:
                    if x == m - 1 and y == n - 1:
                        return res
                    else:
                        dp[x][y] = 1
                        new_stack.append((x, y))
                # case 4:
                x, y = coord[0] - 2, coord[1] + 1
                if x >= 0 and y < n and not grid[x][y] and not dp[x][y]:
                    if x == m - 1 and y == n - 1:
                        return res
                    else:
                        dp[x][y] = 1
                        new_stack.append((x, y))  
            stack = new_stack
        return -1
                    
