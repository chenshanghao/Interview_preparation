import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        res = ""
        start = n
        k = k-1
        while(len(nums) > 0):
            start -= 1
            # print(math.factorial(start))
            index = k // math.factorial(start)
            new_val = nums[index]
            nums.pop(index)
            k = k % math.factorial(start)
            res += str(new_val)
        return res
            
            
        
        
        