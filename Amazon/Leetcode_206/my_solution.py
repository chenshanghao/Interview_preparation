"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        dummy = ListNode(-1)
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
