class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        n = len(nums)
        hash = {}
        res = []
        for num in nums:
            if num in hash:
                res.append(num)
            hash[num] = 1
        for num in range(1, n+1):
            if num not in hash:
                res.append(num)
                break
        return res