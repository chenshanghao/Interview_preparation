# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # edge case
        if not head or not head.next:
            return True
        # find mid
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        # reverse half linkedlist
        slow = self.reversedLinkedList(slow)
        # check 
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
    
    def reversedLinkedList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
        
        