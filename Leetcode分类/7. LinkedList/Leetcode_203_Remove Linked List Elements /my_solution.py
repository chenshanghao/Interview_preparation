# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, curr = dummy, head
        while curr:
            if curr.val == val:
                pre.next = curr.next
                curr = curr.next
                continue
            curr = curr.next
            pre = pre.next
        return dummy.next
                
        