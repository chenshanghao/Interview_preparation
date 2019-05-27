# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tmp = ListNode(-1)
        carry = 0
        while l1 or l2:
            nodeVal = carry
            if l1:
                nodeVal += l1.val
                l1 = l1.next
            if l2:
                nodeVal += l2.val
                l2 = l2.next
            if nodeVal >= 10:
                nodeVal %= 10
                carry = 1
            else:
                carry = 0
            tmp.next = ListNode(nodeVal)
            tmp = tmp.next
        if carry:
            tmp.next = ListNode(1)
        return dummy.next
        