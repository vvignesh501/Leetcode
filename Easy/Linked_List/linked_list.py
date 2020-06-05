#from linkedList import LinkedList

class Solution:

    def __init__(self, num):
        self.next = None
        self.data = num

    def hasCycle(self, head) -> bool:
        fast = head
        slow = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False


g = Solution([3,2,0,-4])
out = g.hasCycle()
print(out)