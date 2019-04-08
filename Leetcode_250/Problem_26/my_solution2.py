class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        i, j = 1, 1
        while(j < n):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i