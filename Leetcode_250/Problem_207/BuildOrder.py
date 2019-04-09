import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        outlist = [[] for _ in range(numCourses)]
        
        for p in prerequisites:
            indegree[p[0]] += 1
            outlist[p[1]].append(p[0])
        
        queue = collections.deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        k = 0
        while queue:
            x = queue.popleft()
            k += 1
            for i in outlist[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return k == numCourses
                
    
    