class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        res = []
        if len(numbers) <= 2:
            return res
        numbers = sorted(numbers)
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            target = 0 - numbers[i]
            j, k = i+1, len(numbers) - 1
            while(j < k):
                if j > i + 1 and numbers[j - 1] == numbers[j]:
                    j += 1
                    continue
                if k < len(numbers) -1 and numbers[k] == numbers[k+1]:
                    k -= 1
                    continue
                if numbers[j] + numbers[k] == target:
                    res.append([numbers[i], numbers[j], numbers[k]])
                    j += 1
                    k -= 1  
                elif numbers[j] + numbers[k] > target:
                    k -= 1
                else:
                    j += 1
                
        return res