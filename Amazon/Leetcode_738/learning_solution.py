class Solution:
    """
    @param num: a non-negative integer N
    @return: the largest number that is less than or equal to N with monotone increasing digits.
    """
    def monotoneDigits(self, num):
        # write your code here
        
        # 从高位向低位遍历整数N的各位数，找到第一个违反单调不减的数的下标x
        # 将x位后的所有数替换为0，记得到的新数为M，则M - 1即为答案
        strNums = str(num)
        n = len(strNums)
        if n < 2:
            return num
        
        idx = -1
        for i in range(n - 1, 0, -1):
           
            if strNums[i] <= strNums[i-1]:
            # 111111110  return 111111109 need:99999999 所以要<=
                idx = i
        if idx == -1:
            return num
        
        res = ''
        for i in range(idx):
            res += strNums[i]
        res += '0' * (n - idx)
        return int(res) - 1
            
            