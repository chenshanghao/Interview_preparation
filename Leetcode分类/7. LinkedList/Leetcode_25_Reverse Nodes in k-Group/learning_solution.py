# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy
        while temp:
            temp = self.reverseNextK(temp, k)
        return dummy.next
    
    
    def reverseNextK(self, head, k):
        # Check if there are k nodes left
        temp = head
        for i in range(k):
            if not temp.next:
                return None
            temp = temp.next

        # The last node when the k nodes reversed
        node = head.next
        prev = head
        curr = head.next
        # Reverse k nodes
        for i in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # Connect with head and tail
        node.next = curr
        head.next = prev
        return node