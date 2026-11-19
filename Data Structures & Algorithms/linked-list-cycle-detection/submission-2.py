# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ht = {}
        curr = head

        while curr and curr.next:
            if curr.val not in ht:
                ht[curr.val] = 1
                curr = curr.next
            else:
                return True
        return False