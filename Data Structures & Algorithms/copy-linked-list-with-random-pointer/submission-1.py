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

        while curr:
            new = Node(curr.val)

            hm[curr] = new
            curr = curr.next
        
        curr = head
        new = hm.get(curr)
        while curr:
            new.random = hm.get(curr.random)
            new.next = hm.get(curr.next)
            new = new.next
            curr = curr.next
            
        return hm.get(head)