"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if not head or not head.next:
            return True
        fast = slow = head
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        slow = self.reverseLinkedlist(slow)
        while(slow):
            if slow.val == head.val:
                slow = slow.next
                head = head.next
            else:
                return False
        return True
    
    def reverseLinkedlist(self, head):
        if not head or not head.next:
            return head
        
        dummy  = ListNode(-1)
        while(head):
            tmp = head 
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
            
        
