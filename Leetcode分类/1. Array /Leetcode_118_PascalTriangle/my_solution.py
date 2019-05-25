class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            lastRow = res[i - 1]
            for i in range(len(lastRow) - 1):
                tmp.append(lastRow[i] + lastRow[i + 1])
            tmp.append(1)
            res.append(tmp)
        return res
        