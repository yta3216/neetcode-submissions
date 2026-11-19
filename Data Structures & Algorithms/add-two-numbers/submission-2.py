# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        a = l1
        b = l2

        new = None
        prev = ListNode()
        head = None

        carry = 0

        while a or b:
            res = 0
            if a:
                res += a.val
            if b:
                res += b.val

            if carry > 0:
                res += 1
                carry = 0
            if res > 9:
                carry += 1
                res = res % 10
            
            new = ListNode(res)
            prev.next = new

            if not head:
                head = new
            prev = prev.next
            
            if a:
                a = a.next
            if b:
                b = b.next
        if carry > 0:
            prev.next = ListNode(carry)
        return head
            

        