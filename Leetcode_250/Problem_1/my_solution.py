class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict_key_pos = {}
        for i in range(n):
            if target - nums[i] in dict_key_pos:
                return [dict_key_pos[target - nums[i]], i]
            else:
                dict_key_pos[nums[i]] = i  
        