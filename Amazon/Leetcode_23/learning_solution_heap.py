from heapq import heappush, heappop, heapify,heapreplace
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        n = len(lists)
        if not n:
            return None
        dummy = temp = ListNode(-1)
        
        h = [(l.val, l) for l in lists if l]
        heapify(h)
        
        while h:
            val, node = heappop(h)
            temp.next = node
            temp = temp.next
            node = node.next
            if node:
                heappush(h, (node.val, node))
        return dummy.next