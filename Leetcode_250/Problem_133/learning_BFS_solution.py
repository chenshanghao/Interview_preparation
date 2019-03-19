import collections
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dict_node_clonenode = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dict_node_clonenode:
                    neighborCopy = Node(neighbor.val, [])
                    dict_node_clonenode[neighbor] = neighborCopy
                    dict_node_clonenode[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dict_node_clonenode[node].neighbors.append(dict_node_clonenode[neighbor])
        return nodeCopy
        
        