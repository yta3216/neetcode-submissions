# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle
        slow = head
        fast = head
        length = 1
        while fast.next:
            if (length % 2 == 0):
                slow = slow.next
            fast = fast.next
            length += 1
        
        # cut middle
        tmp = slow.next
        slow.next = None

        # reverse right half
        curr = tmp
        prev = None
        while curr:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new

        # construct new list
        start = head
        end = prev

        n = 0
        while start or end:
            if (n % 2 == 0):
                tmp = start.next
                start.next = end

                start = tmp
            else:
                tmp = end.next
                end.next = start

                end = tmp
            n += 1

