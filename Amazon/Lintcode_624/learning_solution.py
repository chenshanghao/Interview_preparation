class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        queue = [s]
        hash = set([s])
        resMin = len(s)
        
        while queue:
            s = queue.pop(0)
            for subStri in dict:
                found = s.find(subStri)
                if found != -1:
                    new_s = s[:found] + s[found + len(subStri):]
                    if new_s not in hash:
                        resMin = min(resMin, len(new_s))
                        queue.append(new_s)
                        hash.add(new_s)
        return resMin