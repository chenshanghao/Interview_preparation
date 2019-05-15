class Solution:

    def removeObstacle(self, m, n, lot):
        self.res = float('inf')
        self.helper(lot, 0, 0, 0)
        return self.res


    def helper(self, lot, i, j, step):
        if i < 0 or j < 0 or i == len(lot) or j == len(lot[0]) or lot[i][j] == 0:
            return

        if lot[i][j] == 9:
            self.res = min(step, self.res)

        lot[i][j] = 0
        self.helper(lot, i - 1, j, step + 1)
        self.helper(lot, i + 1, j, step + 1)
        self.helper(lot, i, j + 1, step + 1)
        self.helper(lot, i + 1, j - 1, step + 1)
        lot[i][j] = 1