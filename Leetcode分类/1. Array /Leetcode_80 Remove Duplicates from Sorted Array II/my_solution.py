class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsLength = len(nums)
        if numsLength <= 2:
            return numsLength
        index, cnt = 0, 1
        for i in range(1, numsLength):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
                cnt = 1
            elif nums[i] == nums[index] and cnt == 1:
                index += 1
                nums[index] = nums[i]
                cnt += 1
        return (index + 1)