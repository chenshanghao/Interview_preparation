# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        oddList = tmpOdd = ListNode(-1)
        evenList = tmpEven = ListNode(-1)
        while head:
            tmpOdd.next = head
            tmpOdd = tmpOdd.next
            tmpEven.next = head.next
            tmpEven = tmpEven.next
            if not head.next or not head.next.next:
                break
            else:
                head = head.next.next
        tmpOdd.next = evenList.next
        return oddList.next
            