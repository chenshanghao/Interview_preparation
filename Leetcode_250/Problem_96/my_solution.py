class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Catalan number 
        # 用递推式表示就是 h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2) ，
        # 其中h(0)=h(1)=1
        a = [1, 1]
        for i in range(2, n+1):
            temp = 0
            for j in range(1, i+1):
                temp += a[j-1] * a[i-j]
            a.append(temp)
        return a[n]
        