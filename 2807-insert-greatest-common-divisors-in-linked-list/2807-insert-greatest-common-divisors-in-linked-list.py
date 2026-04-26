# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = head , head.next
        while curr:
            gcd = math.gcd(prev.val, curr.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = curr
            prev = curr
            curr = curr.next
        return head
        