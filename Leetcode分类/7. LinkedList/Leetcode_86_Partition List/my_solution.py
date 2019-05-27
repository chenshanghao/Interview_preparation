# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lowerList = lowerTail = ListNode(-1)
        higherList = higherTail = ListNode(-1)
        while head:
            tmp = head
            print(tmp.val)
            head = head.next
            if tmp.val < x:
                lowerTail.next = tmp
                lowerTail = lowerTail.next
            else:
                higherTail.next = tmp
                higherTail = higherTail.next
                
        higherTail.next = None
        lowerTail.next = higherList.next
        
        return lowerList.next