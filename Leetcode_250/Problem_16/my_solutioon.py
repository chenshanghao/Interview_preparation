class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dis = float('inf')
        res = nums[0] + nums[1] + nums[2]
        for i,v in enumerate(nums):
            left = i+1
            right = n-1
            
            while(left < right):
            
                total = v + nums[left] + nums[right]        
                new_dis = abs(total - target)
                if new_dis < dis:
                    res = total
                    dis = new_dis

                if total == target:
                    return target
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return res
            
        