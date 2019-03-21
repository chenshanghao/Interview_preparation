import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  0 -----> 1
        # p[1]     p[0]
        int_degree = [0] * numCourses
        out_list = [[] for _ in range(numCourses)]
        for p in prerequisites:
            int_degree[p[0]] += 1
            out_list[p[1]].append(p[0])
        
        queue = collections.deque()
        for i in range(numCourses):
            if int_degree[i] == 0:
                queue.append(i)
        k = 0
        while queue:
            x = queue.popleft()
            k += 1
            for i in out_list[x]:
                int_degree[i] -= 1
                if int_degree[i] == 0:
                    queue.append(i)
        return k == numCourses
                
        