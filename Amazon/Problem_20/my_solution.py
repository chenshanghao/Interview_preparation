class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        n = len(s)
        # First step： eliminate odd length
        if n % 2 == 1:
            return False
        dict_bracket = {')': '(', '}':'{', ']':'['}
        stack = []
        
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if dict_bracket[s[i]] != stack.pop():
                    return False
        if not stack:
            return True
        else:
            return False
