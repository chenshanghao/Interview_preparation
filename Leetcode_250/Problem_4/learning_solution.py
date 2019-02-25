# https://shenjie1993.gitbooks.io/leetcode-python/004%20Median%20of%20Two%20Sorted%20Arrays.html

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1, len_2 = len(nums1), len(nums2)
        k = (len_1+len_2)//2
        if (len_1 + len_2) % 2 == 0:
            return (self.helper(nums1, nums2, k) + self.helper(nums1, nums2, k-1))/2
        else:
            return self.helper(nums1, nums2, k)
            
            
    def helper(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k==0:    return min(nums1[0],nums2[0])
        
        len_1, len_2 = len(nums1), len(nums2)
        mid_1, mid_2 = len_1//2, len_2//2
        
        if nums1[mid_1] <= nums2[mid_2]:
            if k > mid_1 + mid_2:
                return self.helper(nums1[mid_1+1:], nums2, k-mid_1-1)
            else:
                return self.helper(nums1, nums2[:mid_2], k)
        else:
            if k > mid_1 + mid_2:
                return self.helper(nums1, nums2[mid_2+1:], k-mid_2-1)
            else:
                return self.helper(nums1[:mid_1],nums2, k)
        