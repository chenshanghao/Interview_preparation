import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        dict_word_num = {}
        banned = set(banned)
        paragraph = re.findall(r'\w+', paragraph.lower())
        for word in paragraph:
            word = word.lower()
            if word in banned:
                continue
            if word in dict_word_num:
                dict_word_num[word] += 1
            else:
                dict_word_num[word] = 1
        maxWord, maxNum = None, 0
        for word, num in dict_word_num.items():
            if dict_word_num[word] > maxNum:
                maxNum = dict_word_num[word]
                maxWord = word
        return maxWord