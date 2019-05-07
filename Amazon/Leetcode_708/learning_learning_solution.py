"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        tmp = ListNode(x)
        if not node:
            tmp.next = tmp
            return tmp
            
        cur, prev = node.next, node
        while True:
            if prev.val <= tmp.val <= cur.val:
                break
            if prev.val > cur.val and (tmp.val < cur.val or tmp.val > prev.val):
                break
            if cur == node:
                break
            cur, prev = cur.next, prev.next
        
        prev.next = tmp
        tmp.next = cur
        return node