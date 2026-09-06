# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for _ in range(k):
            if curr is None:
                return head
            curr = curr.next
        prev = curr
        curr = head

        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head.next = self.reverseKGroup(curr, k)

        return prev