class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumericS = [c for c in s.lower() if c.isalnum()]
        return alphanumericS == alphanumericS[::-1]