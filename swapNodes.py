# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def swapPairs(self, head):
        if not head or not head.next: return head
        cur = head
        head = cur.next
        nxt = head.next
        head.next = cur
        cur.next = self.swapPairs(nxt)
        return head


c = Solution()
node = ListNode([1])
node.next = ListNode([2])
node.next.next = ListNode([3])
node.next.next.next = ListNode([4])
res = c.swapPairs(node)
print(res)
