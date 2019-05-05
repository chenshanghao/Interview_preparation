class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        # Write your code here
        dictNum ={}
        res = 0
        if k == 0:
            for num in nums:
                if num in dictNum:
                    dictNum[num] += 1
                    if dictNum[num] == 2:
                        res += 1
                else:
                    dictNum[num] = 1
                    
        for num in nums:
            if num in dictNum:
                continue
            else:
                if k + num in dictNum or num - k in dictNum:
                    res += 1
                dictNum[num] = 1
        return res