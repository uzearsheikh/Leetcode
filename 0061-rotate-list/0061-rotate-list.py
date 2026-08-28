class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 1
        fast = head
        while fast and fast.next:
            fast = fast.next
            length+=1
       
        k = k%length
        if k == 0:
            return head
        tail = head
        for i in range(length-k-1):
            tail = tail.next
        new_head = tail.next
        fast.next = head
        tail.next = None

        return new_head

        