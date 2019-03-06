from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end = 0, 0
        # the count of char needed by current window, negative means current window has it but not needs it
        char_need = defaultdict(int)
        # count of chars not in current window but in t
        count_need = len(t)
        min_start = 0
        min_length = float('inf')
        
        for i in t:
            char_need[i] += 1
        while end < len(s):
            if char_need[s[end]] > 0:
                # current window needs all char in t
                count_need -= 1
            # current window contains s[end] now, so does not need it any more
            char_need[s[end]] -= 1
            end += 1
            while count_need == 0:
                if min_length > (end - start):
                    min_length = end - start
                    min_start = start
            # current window does not contain s[start] any more
                char_need[s[start]] += 1
            # when some count in char_need is positive, it means there is char in t but not current window

                if char_need[s[start]] > 0:
                    count_need += 1
                start += 1
        return "" if min_length == float('inf') else s[min_start:min_start + min_length]


        
                
            