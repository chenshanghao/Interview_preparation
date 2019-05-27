# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        headTail = slow
        slow = slow.next
        headTail.next = None
        slow = self.reverseLinkedList(slow)
        
        dummy = tmp = ListNode(-1)

        while head or slow:
            if head:
                tmp.next = head
                head = head.next
                tmp = tmp.next
            if slow:  
                tmp.next = slow
                slow = slow.next
                tmp = tmp.next
        return dummy.next
            
        
    
    def reverseLinkedList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
        