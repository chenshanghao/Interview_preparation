class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m = len(matrix)
        n = len(matrix[0])
        l, h = 0, m * n - 1
        while l <= h:
            mid = l + (h - l) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False