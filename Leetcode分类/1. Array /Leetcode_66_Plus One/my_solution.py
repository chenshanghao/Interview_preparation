class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        n = len(digits)
        i = n - 1
        while carry and i >= 0:
            tmp = carry
            carry  = (digits[i] + tmp) // 10
            digits[i] = (digits[i] + tmp) % 10
            i -= 1
            
        if carry:
            digits.insert(0, 1)
        return digits