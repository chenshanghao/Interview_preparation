
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        dict_key_index = {}
        result_len = 0
        for i in strs:
            sorted_i = str(sorted(i))
            if sorted_i in dict_key_index:
                result[dict_key_index[sorted_i]].append(i)
            else:
                dict_key_index[sorted_i] = result_len
                result.append([i])
                result_len += 1
        return result