class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n, i = len(nums), 0
        if n == 0: return 1
 
        while i < n:
            # 获取当前位置的数据，减去1是为了得到 在list要插入的位置
            w = nums[i] - 1 
            # 0 < nums[i] <= n 判断是否出界
            # nums[i] != nums[w] 如果相等或者是本身就没必要替换了，避免死循环
            if 0 < nums[i] <= n and nums[i] != nums[w]:  
                nums[i], nums[w] = nums[w], nums[i]      
            else:
            # 当前位置上的数，没有找到合适的位置，进行下一个位置
                i += 1  
 
        for i in range(n):  # 遍历返回
            if i + 1 != nums[i]:
                return i + 1
        return (n + 1)

                
                
        
        