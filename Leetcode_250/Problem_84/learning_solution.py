# https://blog.csdn.net/princexiexiaofeng/article/details/79652003

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
            print(stack)
        # heights.pop()
        return result
        