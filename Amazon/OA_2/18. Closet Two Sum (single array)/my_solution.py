class Solution:

    def findClosest(self, arr, target):
        arr = sorted(arr)
        res = float('inf')
        i, j = 0, len(arr) - 1
        while(i < j):
            sum_val = arr[i] + arr[j]
            if sum_val > target:
                j -= 1
            elif sum_val < target:
                i += 1
            else:
                return 0
            res = min(abs(sum_val - target), res)
        return res
