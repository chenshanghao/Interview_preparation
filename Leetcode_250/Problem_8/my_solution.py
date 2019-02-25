class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        n = len(str)
        if not n:   return res
        
        i, sign = 0, 1
        while(i<n):
            if str[i] == '-':
                sign = -1
                i +=1
                break
            elif str[i] == '+':
                i +=1
                break
            elif str[i].isdigit():
                break
            elif str[i] == ' ':
                i+=1
            else:
                return res
        while(i<n and str[i].isdigit()):
            res = res*10 + int(str[i])
            i += 1
        res *= sign
        if res > pow(2,31)-1:
            return pow(2,31)-1
        elif res < -pow(2,31):
            return -pow(2,31)
        else:
            return res
            
        

        
        