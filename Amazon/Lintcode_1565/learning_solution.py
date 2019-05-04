class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        n = length
        if n <= 7:
            return 1
        dp = [float('inf')] * (n+1)
        for i in range(8):
            dp[i] = 1
        dictConnections = {}
        for connection in connections:
            dictConnections[connection[0]] = connection[1]
        
        for i in range(1, n + 1):
            if i <= 7 and i in dictConnections:
                dp[dictConnections[i]] = 1
                continue
            if i > 7:
                for j in range(1,7):
                    dp[i] = min(dp[i], dp[i-j]+1)
            if i in dictConnections:
                dp[dictConnections[i]] = min(dp[dictConnections[i]], dp[i])
        return dp[n]