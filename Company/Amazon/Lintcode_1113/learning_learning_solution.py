class Solution:
    """
    @param equation: a string
    @return: return a string
    """
    def solveEquation(self, equation):
        # write your code here
        if not equation:
            return 'No solution'
        left, right = equation.split('=')[0], equation.split('=')[1]
        leftNum, leftX = self.helper(left)
        rightNum, rightX = self.helper(right)
        print(leftNum, leftX)
        print(rightNum, rightX)
        
        if leftX == rightX:
            if leftNum == rightNum:
                return 'Infinite solutions'
            return 'No solution'
        res = (rightNum - leftNum) / (leftX - rightX)
        return "x=" + str(res)
        
    
    def helper(self, s):
        xNum = 0
        Num = 0
        sign = 1
        
        digit = 0
        for char in s:
            if char.isdigit():
                digit = digit * 10 + int(char)
            elif char == 'x':
                if digit == 0:
                    xNum += 1
                else:
                    xNum += sign * digit
                    digit = 0
            else:
                Num += sign * digit
                digit = 0
                sign = 1 if char == '+' else -1
        Num += sign * digit
        return Num, xNum
        