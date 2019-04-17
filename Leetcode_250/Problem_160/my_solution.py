# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        len_a, len_b = self.getLengthOfLinkedlist(headA), self.getLengthOfLinkedlist(headB)
        while(len_a > len_b):
            headA = headA.next
            len_a -= 1
        
        while(len_b > len_a):
            headB = headB.next
            len_b -= 1
            
        while(headA):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
        
        
        
    def getLengthOfLinkedlist(self, head):
        link_len = 0
        while(head):
            link_len += 1
            head = head.next
        return link_len
        