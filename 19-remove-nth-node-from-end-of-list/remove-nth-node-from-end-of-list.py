# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        # delete head
        if n == length:
            return head.next
        
        curr = head
        
        for i in range(length - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head