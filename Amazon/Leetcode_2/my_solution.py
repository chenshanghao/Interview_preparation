class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dict_val_index = {}
        for index, val in enumerate(numbers):
            if target - val in dict_val_index:
                return [dict_val_index[target - val], index]
            else:
                dict_val_index[val] = index
        return None
            