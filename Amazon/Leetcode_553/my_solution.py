class Solution:
    """
    @param nums: an array
    @return: the corresponding expression in string format
    """
    def optimalDivision(self, nums):
        # Write your code here
        n = len(nums)
        nums = [str(i) for i in nums]
        if n <= 2: 
            return '/'.join(nums)

        lenNum1 = len(nums[0])
        res = '/'.join(nums)
        res = res[0:lenNum1+1] + '(' + res[lenNum1+1:] + ')'
        return res
            