# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        li = []
        curr = head

        while curr:
            li.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(li) - 1
        print(li)
        while (l < r):
            if (li[l] == li[r]):
                l += 1
                r -= 1
            elif (l == r):
                return True
            else:
                return False

        return True