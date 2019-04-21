"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        dummy = temp = ListNode(-1)

        while(True):
            min_val = float('inf')
            index = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    index = i
            if index == -1:
                break
            else:
                temp.next = lists[index]
                lists[index] = lists[index].next
                temp = temp.next
                
        return dummy.next
                
        
                

