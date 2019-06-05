class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        str = str.split()
        str = str[::-1]
        return ' '.join(str)