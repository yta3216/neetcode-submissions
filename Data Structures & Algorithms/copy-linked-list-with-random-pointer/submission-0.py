"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}

        curr = head
        new = None
        new_head = None

        while curr:
            new = Node(curr.val)
            if not new_head:
                new_head = new

            hm[curr] = new
            curr = curr.next
        
        curr = head
        new = new_head
        while curr:
            new.random = hm.get(curr.random)
            new.next = hm.get(curr.next)
            new = new.next
            curr = curr.next
            
        return new_head