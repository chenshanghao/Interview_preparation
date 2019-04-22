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
        if lists == []:
            return None 
        while(len(lists)!=1):
            l=[]
            a=0
            while(a+1<len(lists)):
                t=self.mergeTwoLists(lists[a],lists[a+1])
                l.append(t)
                a=a+2
            if len(lists)%2==1:l.append(lists[-1])
            lists=l
        return lists[0]       
        
        
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
            
        

                
        
                

