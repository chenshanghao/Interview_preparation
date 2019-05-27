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
        aLength, bLength = 0, 0
        tmpA, tmpB = headA, headB
        while tmpA:
            aLength += 1
            tmpA = tmpA.next
        while tmpB:
            bLength += 1
            tmpB = tmpB.next
        
        if aLength > bLength:
            for i in range(aLength - bLength):
                headA = headA.next
        elif bLength > aLength:
            for i in range(bLength - aLength):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
            
        