class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def getRow(self, rowIndex):
        # write your code here
        if rowIndex == 0:
            return [1]
        res = [1, 1]
        for i in range(2, rowIndex + 1):
            new_res = []
            for j in range(len(res) - 1):
                new_res.append(res[j] + res[j + 1])
            res = [1] + new_res + [1]
        return res
                