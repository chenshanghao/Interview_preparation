class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分法的关键在于取中间值后，与目标值比较，判断左半段还是右半段。
        # 观察上述八种情况，可以发现以中间值为界，左右两部分总有一段是绝对升序的。
        # 当 nums[mid] < nums[right] 时，右半段绝对升序；
        # 当 nums[mid] > nums[right] 时，左半段绝对升序
        n = len(nums)
        if n==0:
            return -1
        l,r = 0, n-1
        while(l<r):
            mid = (l+r) // 2
            print(l,r,mid)
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]:
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid -1
            elif nums[mid] > nums[r]:
                if nums[l] <= target and nums[mid] > target:
                    r = mid -1
                else:
                    l = mid +1 
        if l == r and nums[l] == target:
            return l
        else:
            return -1
                