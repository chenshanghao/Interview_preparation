# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tmp = head
        while head.next:
            head = head.next
            if head.val != tmp.val:
                tmp.next = head
                tmp = tmp.next
        tmp.next = None
        return dummy.next
            
        
        