# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # edge case 1
        if not head:
            return head
        
        listLength = 0
        tmp = head
        while tmp:
            listLength += 1
            nextTail = tmp 
            tmp = tmp.next
        k = k % listLength
        
        # edge case 2
        if k == 0:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        preTail, nextHead = dummy, dummy.next
        for i in range(listLength - k):
            preTail = preTail.next
            nextHead = nextHead.next
        preTail.next = None
        
        dummy.next = nextHead
        nextTail.next = head
        
        return dummy.next