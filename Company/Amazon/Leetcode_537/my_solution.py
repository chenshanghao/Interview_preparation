class Solution:
    """
    @param a: a string
    @param b: a string
    @return: a string representing their multiplication
    """
    def complexNumberMultiply(self, a, b):
        # Write your code here
        aReal, aImaginary = self.getRealImaginaryNum(a)
        bReal, bImaginary = self.getRealImaginaryNum(b)
        
        resReal = aReal * bReal - aImaginary * bImaginary
        resImaginary = aReal * bImaginary + bReal * aImaginary
        
        res = str(resReal) + '+' + str(resImaginary) + 'i'
        return res
        
        
        
    def getRealImaginaryNum(self, s):
        real, imaginary = 0, 0
        if '+' in s:
            idx = s.find('+')
            real, imaginary = int(s[:idx]), int(s[idx+1:-1])
        return (real, imaginary)