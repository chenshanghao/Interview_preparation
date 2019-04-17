# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd_list = temp1 = ListNode(-1)
        even_list = temp2 = ListNode(-1)
        while(head):
            temp1.next = head
            temp1 = temp1.next
            temp2.next = head.next
            temp2 = temp2.next
            if not head.next or not head.next.next:
                break
            else:
                head = head.next.next
        temp1.next = even_list.next
        return odd_list.next
            
            
        
        