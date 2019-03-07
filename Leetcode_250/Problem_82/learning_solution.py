# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        while(head and head.next):
            if head.val == head.next.val:
                while(head.next.next and head.next.val == head.next.next.val):
                    head = head.next
                head = head.next.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
                
        