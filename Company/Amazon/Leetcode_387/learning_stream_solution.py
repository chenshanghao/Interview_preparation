class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        # Non-counting algorithm. Using double linked list and hash map
        dup = set()
        chars = {}
        head = LinkedNode()
        tail = head
        for c in str:
            if c in dup: continue
            if c in chars:
                node = chars[c]
                
                prev = node.prev
                next = node.next
                prev.next = next

                if next:
                    next.prev = prev
                if node == tail:
                    tail = prev

                del chars[c]
                dup.add(c)
            else:
                node = LinkedNode()
                node.val = c
                node.prev = tail
                chars[c] = node
                tail.next = node
                tail = node
        return head.next.val

class LinkedNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.val = '^'