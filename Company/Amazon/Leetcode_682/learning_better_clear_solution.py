class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    #用数组保存分数，按照题意模拟即可
    def calPoints(self, ops):
        # Write your code here
        # Time: O(n)
        # Space: O(n)
        history = []
        for op in ops:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)