class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        # Write your code here
        dis = float('inf')
        if len(array) < 2:
            return dis
        array = sorted(array)
        i, j = 0, len(array) - 1
        while(i < j):
            if array[i] + array[j] > target:
                j -= 1
            elif array[i] + array[j] < target:
                dis = min(dis, target - (array[i] + array[j]))
                i += 1
            else:
                return target
        if dis == float('inf'):
            return -1
        return target - dis