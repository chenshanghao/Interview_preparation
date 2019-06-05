# https://segmentfault.com/a/1190000013805875


class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        # Write your code here
        self.father = {}
        for i in range(len(ListA)):
            if ListA[i] not in self.father:
                self.father[ListA[i]] = ListA[i]
            if ListB[i] not in self.father:
                self.father[ListB[i]] = ListB[i]
            self.union(ListA[i], ListB[i])
        print(self.father)
           
        result = {} #key: root of the group, values: the book under the same father
        for key in self.father:
            root = self.find(key)
            if root not in result:
                result[root] = []
                
            result[root].append(key)
        print(result)
        max_size = 0
        for key in result:
            if max_size < len(result[key]):
                max_size = len(result[key])
                max_key = key 
        
        return result[max_key]
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            
    def find(self, x):
        j = x 
        while self.father[j] != j:
            j = self.father[j]
        while self.father[x] != j:
            fx = self.father[x]
            self.father[x] = j 
            x = fx 
        return j