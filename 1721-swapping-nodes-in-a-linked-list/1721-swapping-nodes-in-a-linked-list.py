# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        for i in range(1,k):
            temp = temp.next
        length = 1
        tail = head
        while tail and tail.next :
            tail = tail.next 
            length+=1
        vemp = head
        for i in range(1,length - (k-1)):
            vemp = vemp.next
        temp.val,vemp.val=vemp.val,temp.val
        return head
        
