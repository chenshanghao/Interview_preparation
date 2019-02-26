class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        results = []
        len_nums = len(nums)
        nums.sort()
        for i in range(len(nums)-3):
            a = nums[i]
            target_i = target - a
            for j in range(i+1, len(nums)-2):
                b = nums[j]
                left = j + 1
                right = len(nums) - 1
       
                while(left < right):
                    c = nums[left]
                    d = nums[right]
                    current_sum = b + c + d

                    # 错误1的起因
                    if current_sum == target_i:
                        if [a, b, c, d] not in results:
                            results.append([a, b, c, d])
                        while(left < right and nums[left] == nums[left + 1]):
                            left += 1
                        while(left < right and nums[right] == nums[right - 1]):
                            right -= 1
                        left += 1
                        right -= 1
                    elif current_sum > target_i:
                        right -= 1
                    elif current_sum < target_i:
                        left += 1
        return results