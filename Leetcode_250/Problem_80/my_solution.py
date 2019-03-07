class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:  return 0
        slow, fast = 0, 0
        count = 0
        val = float('inf')
        
        while(fast < n):
            print(slow, fast)
            if nums[fast] != val:
                nums[slow] = nums[fast]
                val = nums[fast]
                count = 1
                slow += 1
                fast += 1
            elif nums[fast] == val:
                if count < 2:
                    nums[slow] = nums[fast]
                    count += 1
                    slow += 1
                    fast += 1
                else:
                    count += 1
                    fast += 1
        return (slow)
        