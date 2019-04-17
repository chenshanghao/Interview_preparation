# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        dummy = temp = ListNode(-1)
        carry = 0
        while(l1 or l2):
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(val)
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return dummy.next
        
        