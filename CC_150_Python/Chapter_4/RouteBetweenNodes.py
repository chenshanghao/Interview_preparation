from collections import defaultdict
# https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/

class Graph:
    def __init__(self, vertices):
        self.V = vertices                   # number of vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def isReachable(self, s, d):
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 

        # create a queue for BFS
        queue=[]

        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True

        while queue:
            #Dequeue a vertex from queue  
            n = queue.pop(0) 
              
            # If this adjacent node is the destination node, 
            # then return true 
            if n == d: 
                return True
  
            #  Else, continue to do BFS 
            for i in self.graph[n]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
        # If BFS is complete without visited d 
        return False


# Create a graph given in the above diagram 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
u, v =1, 3
  
if g.isReachable(u, v): 
    print("There is a path from %d to %d" % (u,v)) 
else : 
    print("There is no path from %d to %d" % (u,v)) 
  
u, v =3, 1
if g.isReachable(u, v) : 
    print("There is a path from %d to %d" % (u,v)) 
else : 
    print("There is no path from %d to %d" % (u,v)) 
  
#This code is contributed by Neelam Yadav

