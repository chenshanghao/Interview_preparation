class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        res = []
        dictWordIdex = {}
        i = 0
        for word in strs:
            orderWord = ''.join(sorted(word))
            if orderWord in dictWordIdex:
                res[dictWordIdex[orderWord]].append(word)
            else:
                dictWordIdex[orderWord] = i
                res.append([word])
                i += 1
        return res
            