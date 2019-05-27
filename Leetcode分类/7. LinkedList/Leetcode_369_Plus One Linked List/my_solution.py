"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        head = self.reverseLinkedList(head)
        tmp = head
        carry = 1
        while tmp:
            if tmp.val < 9:
                tmp.val += 1
                carry = 0
                break
            else:
                tmp.val = 0
                carry = 1
                tmp = tmp.next
        head = self.reverseLinkedList(head)
        if carry:
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        else:
            return head
            
    
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