# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        # if not head or not head.next:
        #     return head
        
        dummy_odd = odd = ListNode(0)
        dummy_even = even = ListNode(0)
        
        while(head):
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy_even.next
        return dummy_odd.next
                
        
        
        