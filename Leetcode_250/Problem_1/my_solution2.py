class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict_value_index = {}
        for index, num in enumerate(nums):
            if target - num in dict_value_index:
                return [dict_value_index[target - num], index]
            else:
                dict_value_index[num] = index
                