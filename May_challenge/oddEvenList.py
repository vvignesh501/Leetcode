# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode):
        left = []
        right = []
        for i in range(0, (len(head) - 1)):
            left = ListNode(head)
            if left.next % 2 == 1:
                left.next = left.next.next
                return left.val, left.next


g = Solution()
out = g.oddEvenList([1, 2, 3, 4, 5])
print(out)
