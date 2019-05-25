# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        tail = pre = dummy
        
        for i in range(n):
            tail = tail.next
            
        while tail.next:
            tail = tail.next
            pre = pre.next
        if n == 1:
            pre.next = None
        else:
            pre.next = pre.next.next
        return dummy.next
            
        