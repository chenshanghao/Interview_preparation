class Solution:
    def countAndSay(self, n: int) -> str:
        ret = '1'
        for i in range(1, n):
            ret = self.helper(ret)         
        return ret
    
    def helper(self, ret):
        new_ret = ''
        n = len(ret)
        cur = ret[0]
        count = 1
        i = 1
        while(i<n):
            if ret[i] == cur:
                count+=1
                i+=1
            else:
                new_ret += (str(count) + cur)
                cur = ret[i]
                count = 1
                i += 1
        new_ret += (str(count) + cur)
        return new_ret
            
            