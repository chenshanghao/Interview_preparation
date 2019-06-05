"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        visited = {}
        node = head
        while(node):
            visited[node] = RandomListNode(node.label)
            node = node.next
        
        visited[None] = None
        node = head
        while(node):
            visited[node].next = visited[node.next]
            visited[node].random = visited[node.random]
            node = node.next
        return visited[head]