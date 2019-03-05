class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            digits[i] = (digits[i] + carry)
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
            
        if carry != 0:  digits.insert(0,1)
        return digits
        