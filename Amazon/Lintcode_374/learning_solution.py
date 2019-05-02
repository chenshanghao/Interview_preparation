# aCount = aCount + aCount + 
# :对于a，分为三种情况：第一种情况，直接忽略这个a，使用前边的a，这样的数量是aCount；第二种情况，跟随前边的a，即aa，这样的数量也是aCount；第三种情况，这个a重新作为一个开始，这样的数量是1。所以就有上边的公式成立。
# bCount = aCount + bCount + bCount: 对于b，有三种情况：第一种情况，直接忽略这个b，使用前边的b，这样的数量为bCount；第二种情况，跟随前边的b，即bb，这样的数量是bCount；第三种情况，不使用前边的b，而以这个b直接跟随a，这样的数量为aCount。
# cCount = bCount + cCount + cCount:与b同理。

class Solution:
    """
    @param source: the input string
    @return: the number of subsequences 
    """
    def countSubsequences(self, source):
        # write your code here
        aCount, bCount, cCount = 0, 0, 0
        for i in source:
            if i == 'a':
                aCount = 2 * aCount + 1
            elif i == 'b':
                bCount = 2 * bCount + aCount
            else:
                cCount = 2 * cCount + bCount
        return cCount