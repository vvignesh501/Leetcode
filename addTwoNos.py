# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        currentNode = head
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10

            currentNode.next = ListNode(val)
            currentNode = currentNode.next

        return head.next


def node(l1, l2, l3):
    one = ListNode(l1)
    two = ListNode(l2)
    three = ListNode(l3)
    one.next = two
    two.next = three
    return one


out = Solution()
res = out.addTwoNumbers(l1=node(2, 4, 9), l2=node(5, 6, 4))
print(res)
