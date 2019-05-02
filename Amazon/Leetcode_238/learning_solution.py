# 分两步做，第一步求所有小于当前i的乘积，从左到右循环，用一个变量维护这个乘积，
# 第二步求所有大于当前i的乘积，从右到左循环，同样用一个变量维护这个乘积。



class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        products = [1] * len(nums)
        
        leading = 1 
        for i, num in enumerate(nums):
            products[i] = leading
            leading *= num 

        trailing = 1 
        for i, num in reversed(list(enumerate(nums))):
            products[i] *= trailing
            trailing *= num
        
        return products