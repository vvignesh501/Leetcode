# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = headA
        curB = headB

        # 1. Stop at shorter one (will break first)
        while curA and curB:
            curA = curA.next
            curB = curB.next

        # 2. Let the longer one runs to end, find how much longer it is
        offsetA = 0
        offsetB = 0
        while curA:
            curA = curA.next
            offsetA += 1
        while curB:
            curB = curB.next
            offsetB += 1

        # 3. Start all over, give longer one head start
        curA = headA
        curB = headB
        for i in range(offsetA):
            curA = curA.next
        for i in range(offsetB):
            curB = curB.next

        # 4. Now both have equal length to the end, compare
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None


g = Solution()
out = g.getIntersectionNode([4, 1, 8, 4, 5], [5, 0, 1, 8, 4, 5])
print(out)
