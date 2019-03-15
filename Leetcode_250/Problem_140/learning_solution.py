class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:   # transfer to  adjacency list
            graph[x].append(y)
        
        for v in range(numCourses):
            if visit[v] == 0 and not self.helper(graph, visit, v):
                return False
        return True
            
            
    def helper(self, graph, visit, v):
        visit[v] = -1 #visiting
        
        for w in graph[v]:
            if visit[w] == -1:  return False   # visiting
            if visit[w] == 1:   continue       # visited
            
            if not self.helper(graph, visit, w):    return False
        
        visit[v] = 1
        return True
    
    