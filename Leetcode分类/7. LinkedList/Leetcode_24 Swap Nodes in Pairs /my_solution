# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        while tmp.next and tmp.next.next:
            preNode = tmp.next
            postNode = tmp.next.next
            preNode.next = postNode.next
            tmp.next = postNode
            postNode.next = preNode
            tmp = tmp.next.next
        return dummy.next
        