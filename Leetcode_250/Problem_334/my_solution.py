class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 2:
            return False
        last_last, last = 0, -1
        for i in range(1, n):
            if nums[i] <= nums[last_last]:
                last_last = i         
            else:
                if last == -1:
                    last = i
                else:
                    if nums[i] <= nums[last]:
                        last = i
                    else:
                        return True
        return False
                
        