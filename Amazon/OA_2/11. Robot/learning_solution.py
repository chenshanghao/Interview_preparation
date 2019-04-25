class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        if not len(maze) or not len(maze[0]):
            return -1
        
        if start == destination:
            return 0
        
        m, n = len(maze), len(maze[0])
        distance = [[float('inf') for j in range(n)] for i in range(m)]
        distance[start[0]][start[1]] = 0
        self.helper(maze, start, distance)
        print(distance)
        
        if distance[destination[0]][destination[1]] == float('inf'):
            return -1
        else:
            return distance[destination[0]][destination[1]]
            
    def helper(self, maze, start, distance):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for direction in directions:
            x = start[0] + direction[0]
            y = start[1] + direction[1]
            count = 0
            while(x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0]) and maze[x][y] == 0):
                x += direction[0]
                y += direction[1]
                count += 1
            if distance[start[0]][start[1]] + count < distance[x - direction[0]][y - direction[1]]:
                distance[x - direction[0]][y - direction[1]] = distance[start[0]][start[1]] + count
                self.helper(maze, [x - direction[0], y - direction[1]], distance)
