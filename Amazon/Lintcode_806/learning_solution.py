class Solution:
    """
    @param codeList: The codeList
    @param shoppingCart: The shoppingCart
    @return: The answer
    """
    def buyFruits(self, codeList, shoppingCart):
        # Write your code here
        newCodeList = []
        for itemList in codeList:
            newCodeList += itemList
        lenCodeList, lenShoppingCart = len(newCodeList), len(shoppingCart)
        if lenCodeList > lenShoppingCart:
            return 0
            
        for i in range(lenShoppingCart - lenCodeList + 1):
            idx = 0 
            for j in range(lenCodeList):
                if newCodeList[j] == shoppingCart[j + i] or newCodeList[j] == 'anything':
                    idx += 1
                else:
                    idx = -1
                    break
            if idx == -1:
                continue
            else:
                return 1
        return 0
                    
            