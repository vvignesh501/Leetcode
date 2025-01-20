# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def deleteNode(self, node):
        previousNode = node
        print(previousNode.next)
    while node.next:
        node.val = node.next.val

        previousNode = node

        node = node.next

    previousNode.next = None


g = Solution().deleteNode([4,5,1,9], 5)