# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, A):
        head = ListNode(A)
        fast = head
        slow = head
        if self is not None:
            while fast is not None and fast.next is not None:
                slow = slow.next
        fast = fast.next.next
        return slow
        return slow.next



g = Solution()
out = g.middleNode([1,2,3,4,5])
print(out.__dict__())
print(out)


