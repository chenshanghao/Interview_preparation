class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n < 2:   return
        dis = float('inf')
        nums = sorted(nums)
        res = [nums[0] + nums[1] + nums[2]]
        for i in range(0, n-2):
            left, right = i+1, n-1
            while(left < right):
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val == target:   return target
                new_dis = abs(target - sum_val)
                if new_dis < dis:
                    res = sum_val
                    dis = new_dis
                
                if sum_val < target:
                    left += 1
                else:
                    right -= 1
        return res