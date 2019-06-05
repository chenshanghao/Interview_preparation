# 整体思路大致如下, Java版本源码可能有细微出入, C++版本是最新的源码

# 动态规划, 设定状态 f[i] 表示剩余 i, i+1, ..., n-1 这些硬币时, 先手者可以拿到的最大价值.

# 设 sum[i] = values[i] + values[i+1] + ... + values[n-1].

# 此时后手者拿到的价值即为 sum[i] - f[i].

# 在这个状态设定下, 答案即为 f[0] > sum[0] - f[0].

# 状态转移方程为:

# f[i] = max(
#     sum[i+1] - f[i+1] + values[i],                  // 先手者拿一枚
#     sum[i+2] - f[i+2] + values[i] + values[i+1]       // 先手者拿两枚
# );



class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        
        if n <= 2:
            return True
        
        sum1 = values[n - 1]
        sum2 = values[n - 1] + values[n - 2]
        dp = [0] * n
        dp[n - 1] = values[n - 1]
        dp[n - 2] = values[n - 1] + values[n - 2]
        
        for i in range(n-3, -1, -1):
            dp[i] = max(sum2 - dp[i + 1] + values[i], sum1 - dp[i + 2] + values[i] + values[i + 1])
            sum1 = sum2
            sum2 += values[i]
            
        return sum2 < 2 * dp[0]
            
        
            