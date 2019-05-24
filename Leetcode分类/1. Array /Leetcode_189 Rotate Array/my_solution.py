class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverseArray(nums, 0, n - k - 1)
        self.reverseArray(nums, n - k, n - 1)
        self.reverseArray(nums, 0, n - 1)

        
    
    def reverseArray(self, array, left, right):
        while(left < right):
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        