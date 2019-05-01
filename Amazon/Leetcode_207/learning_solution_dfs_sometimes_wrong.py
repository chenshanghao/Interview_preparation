# topological sorting time complexity: O(V + E)
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        graph = [[] for _ in range(numCourses)]
        visit = [0] * numCourses      # -1 -> visiting  1 -> visited
        for x, y in prerequisites:
            graph[x].append(y)
            
        for v in range(numCourses):
            if visit[v] == 0 and not self.dfs(graph, visit, v):
                return  False
        return True
    
    def dfs(self, graph, visit, v):
        visit[v] = -1
        for w in graph[v]:
            if visit[w] == -1:  return False
            if visit[w] == 1:   continue
            if not self.dfs(graph, visit, w):
                return False
        visit[v] = 1
        return True
        