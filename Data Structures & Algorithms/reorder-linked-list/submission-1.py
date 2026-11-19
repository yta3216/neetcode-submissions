# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# FROM CLAUDE

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # 1. Find end of first half (first half keeps the extra node when n is odd)
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Cut, then reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # 3. Merge: second half is never longer than first,
        #    so it runs out first (or at the same time)
        first = head
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2