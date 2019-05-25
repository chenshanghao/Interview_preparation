# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = tmpPre = ListNode(-1)
        dummy.next = head
        
        for i in range(m - 1):
            tmpPre = tmpPre.next
        
        tmpCur = tmpPre.next
        tail = tmpCur
        for i in range(n - m + 1):
            tmpNode = tmpCur
            tmpCur = tmpCur.next
            tmpNode.next = tmpPre.next
            tmpPre.next = tmpNode
        tail.next = tmpCur
        return dummy.next
        
        