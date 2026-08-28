# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
         # a-1 tak jao
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        # b+1 tak jao
        after = list1
        for _ in range(b + 1):
            after = after.next

        # a-1 ko list2 ke head se jodo
        prev.next = list2

        # list2 ke last node tak jao
        temp = list2
        while temp.next:
            temp = temp.next

        # list2 ke end ko b+1 se jodo
        temp.next = after

        return list1
        