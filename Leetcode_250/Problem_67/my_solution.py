class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return a or b
        m, n = len(a)-1, len(b)-1
        i, j = m, n
        res = ""
        carry = 0
        while(i>=0 or j>=0):
            val = carry
            if i>=0:
                val += int(a[i])
            if j>=0:
                val += int(b[j])
            carry = val // 2
            val = val % 2
            res += str(val)
            i -= 1
            j -= 1
            
        if carry != 0:
            res += str(carry)
        return res[::-1]
        
            