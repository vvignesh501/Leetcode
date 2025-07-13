# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        length = 1
        tail = head
        
        # Move the tail to the end and find the length of the linked list
        while tail.next:
            tail = tail.next
            length += 1
            
        # What if k is > than the length of the list, 
        # perform modulo and get k again from start of head since cyclic
        k = k % length
        if k == 0:
            return head
        
        cur = head
        # Move to the pivot and then rotate
        for i in range(length - k - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        # Above we have already calculated the tail end i.e 4->5->None
        tail.next = head
        
        return newHead
