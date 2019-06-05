import re
class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        banned = set(banned)
        words = re.findall(r'\w+', paragraph)
        dict_word_num = {}
        max_num = 0
        max_word = ''
        for word in words:
            if word in banned:
                continue
            if word in dict_word_num:
                dict_word_num[word] += 1
            else:
                dict_word_num[word] = 1
            
            if dict_word_num[word] > max_num:
                max_num, max_word = dict_word_num[word], word
        
        return max_word
        
            