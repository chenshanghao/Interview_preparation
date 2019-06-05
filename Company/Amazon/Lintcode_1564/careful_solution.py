# 1.intervalList has overlapping intervals
# 2. return Type

class Solution:
    """
    @param intervalList: 
    @param number: 
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        # Write your code here
        for interval in intervalList :
            if(number >= interval[0] and number <= interval[1]):
                return "True"
        return "False"
        