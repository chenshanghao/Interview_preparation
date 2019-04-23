class Solution(object):
    def minPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:  return 0
        n = len(matrix[0])
        if n == 0:  return 0
        
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = matrix[0][0]

        for i in range(1, m):
            dp[i][0] = min(dp[i-1][0], matrix[i][0])

        for j in range(1, n):
            dp[0][j] = min(dp[0][j-1], matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), matrix[i][j])

        return dp[m-1][n-1]


        