class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        indegree = [0] * numCourses
        outlist = [[] for _ in range(numCourses)]
        
        for p in prerequisites:
            indegree[p[0]] += 1
            outlist[p[1]].append(p[0])
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        k = 0
        while queue:
            x = queue.pop(0)
            res.append(x)
            k += 1
            for i in outlist[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        if k == numCourses:
            return res
        else:
            return []
