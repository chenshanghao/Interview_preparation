"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        # 1. decrease order or increase order
        if not l1 or not l2:
            return l2 or l1
            
        dummy = temp = ListNode(-1)
        
        while(l1 and l2):
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if not l1:
            temp.next = l2
        else:
            temp.next = l1
        
        return dummy.next
                
            
