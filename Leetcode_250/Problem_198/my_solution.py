class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n==0:    return 0
        if n<=2:    return max(nums)
        
        sum_array = [0]*(n)
        sum_array[0], sum_array[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            sum_array[i] = max(sum_array[i-1], sum_array[i-2]+nums[i])
        return sum_array[n-1]
        
        