class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        # Write your code here
        stack = []
        for i in ops:
            if i == 'C':
                if stack:
                    stack.pop()
                else:
                    return None
            elif  i == 'D':
                if stack:
                    val = stack.pop()
                    stack.append(val)
                    stack.append(val * 2)
            elif  i == '+':
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    val3 = val1 + val2
                    stack.append(val2)
                    stack.append(val1)
                    stack.append(val3)
                else:
                    return None
            else:
                stack.append(int(i))
        return sum(stack)