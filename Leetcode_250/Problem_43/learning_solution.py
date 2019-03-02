class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                posLow = i + j + 1
                posHigh = i + j
                mul += result[posLow]
                result[posLow] = mul % 10
                result[posHigh] += mul / 10
        # e.g., num1='123', num2='456'; then result = [0, 5, 6, 0, 8, 8], res = [5, 6, 0, 8, 8]
        sb = []
        for res in result:
            if len(sb) != 0 or res != 0: # deal with leading zero issue
                sb.append(res)
        return "0" if len(sb) == 0 else ''.join(str(s) for s in sb)
        