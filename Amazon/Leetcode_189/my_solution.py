class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        k = k % len(nums)
        n = len(nums)
        return nums[n-k:n] + nums[0: n-k]