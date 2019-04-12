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
        fast = ListNode(0)
        fast.next = head
        slow = fast
        for i in range(n):
            fast = fast.next
        while(fast.next):
            slow = slow.next
            fast = fast.next
        if slow.next.next:
            slow.next = slow.next.next
        else:
            head = head.next
        return head
        