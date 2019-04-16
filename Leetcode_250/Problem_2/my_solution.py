# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l2
        dummy = ListNode(-1)
        tmp = dummy
        carry = 0
        while(l1 or l2):
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            if sum_val >= 10:
                sum_val -= 10
                carry = 1
            else:
                carry = 0
            tmp.next = ListNode(sum_val)
            tmp = tmp.next
        if carry:
            tmp.next = ListNode(carry)
            
        return dummy.next
        