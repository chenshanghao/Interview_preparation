class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not n:
            return [-1, -1]
        left, right = 0, n-1
        mid = 0
        while(left<=right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break
        
        
        if nums[mid] != target:
            return [-1, -1]
        
        l, r = mid, mid
        while(l>0 and nums[l-1] == target):
            l -= 1
        while(r< n-1 and nums[r+1] == target ):
            r += 1
        return [l,r]