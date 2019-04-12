# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            tmp = head
            head = head.next
            tmp.next = new_head
            new_head = tmp
        return new_head