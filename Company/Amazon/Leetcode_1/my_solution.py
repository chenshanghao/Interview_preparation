"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        carry = 0
        dummy = temp = ListNode(-1)
        while(l1 or l2):
            new_sum = carry
            if l1:
                new_sum += l1.val
                l1 = l1.next
            if l2:
                new_sum += l2.val
                l2 = l2.next
            if new_sum >= 10:
                new_sum %= 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(new_sum)
            temp = temp.next
        if carry > 0:
            temp.next = ListNode(carry)
        return dummy.next
