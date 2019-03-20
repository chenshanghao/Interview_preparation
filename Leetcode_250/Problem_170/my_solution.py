class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.numbers = []
    def add(self, number):
        # write your code here
        self.numbers.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        dict_value_index = {}
        for idx, number in enumerate(self.numbers):
            if value - number in dict_value_index:
                return True
            else:
                dict_value_index[number] = idx
        return False