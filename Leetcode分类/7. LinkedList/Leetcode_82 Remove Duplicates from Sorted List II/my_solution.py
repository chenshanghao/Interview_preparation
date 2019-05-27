# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tmp = dummy
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                dupVal = curr.val
                while curr.val == dupVal and curr.next:
                    curr = curr.next
                if curr.val == dupVal:
                    tmp.next = None
                    break
            else:
                tmp.next = curr
                curr = curr.next
                tmp = tmp.next
        return dummy.next
        