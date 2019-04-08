# The basic idea is that, for example, nums = [1,2,3,4,5,6,7] and k = 3, 
# first we reverse [1,2,3,4], it becomes[4,3,2,1]; then we reverse[5,6,7], 
# it becomes[7,6,5], finally we reverse the array as a whole, it becomes[4,3,2,1,7,6,5] ---> [5,6,7,1,2,3,4].

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)
        nums[:] = nums[-k:]+nums[0:len(nums)-k]
        
        
        #1.错误1
        # nums[:] = nums[n-k:] + nums[:n-k] 
        # nums = nums[n-k:] + nums[:n-k]
        # The previous one can truly change the value of old nums, 
        # but the following one just changes its reference to a new nums not the value of old nums.
        
        #2.错误2
        # nums[:] = nums[-k:]+nums[0:len(nums)-k]