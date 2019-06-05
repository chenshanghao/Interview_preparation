class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = [[]]
        for num in sorted(nums):
            new_list = []
            for item in res:
                new_list.append(item + [num])
            res += new_list
        return res