# 首先将矩阵的左上角（下标0,0）元素加入堆

# 然后执行k次循环：

# 弹出堆顶元素top，记其下标为i, j

# 将其下方元素matrix[i + 1][j]，与右方元素matrix[i][j + 1]加入堆（若它们没有加入过堆）

import heapq
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        visited = [[False for j in range(n)] for i in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        visited[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans