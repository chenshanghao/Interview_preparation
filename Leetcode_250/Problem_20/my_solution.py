class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 != 0:    return False
        
        stack = []
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if not stack:   return False
                tail = stack.pop()
                if tail != '(': return False
            elif s[i] == ']':
                if not stack:   return False
                tail = stack.pop()
                if tail != '[': return False
            elif s[i] == '}':
                if not stack:   return False
                tail = stack.pop()
                if tail != '{': return False
        
        return True if not stack else False
            
        