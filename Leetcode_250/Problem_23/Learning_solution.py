# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return [] 
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
        