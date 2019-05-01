# topological sorting time complexity: O(V + E)
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
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
                
        k = 0
        while queue:
            x = queue.pop(0)
            k += 1
            for i in outlist[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return k == numCourses