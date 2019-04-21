"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA and not headB:
            return None
            
        len_A, len_B = self.getLengthOfLinkedlist(headA), self.getLengthOfLinkedlist(headB)
        poiter_a, poiter_b = headA, headB
        
        while (len_A > len_B):
            poiter_a = poiter_a.next
            len_A -= 1
            
        while (len_B > len_A):
            poiter_b = poiter_b.next
            len_B -= 1
        
        while poiter_a:
            if poiter_a == poiter_b:
                return poiter_a
            else:
                poiter_a = poiter_a.next
                poiter_b = poiter_b.next
        return None
        
    def getLengthOfLinkedlist(self, head):
        temp = 0
        while head:
            temp += 1
            head = head.next
        return temp
        