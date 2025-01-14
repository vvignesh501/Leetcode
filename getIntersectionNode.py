# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        print(headA, headB)


if __name__ == '__main__':
    llist = Solution.getIntersectionNode(headA=ListNode(x=[4,1,8,4,5]), headB=ListNode(x=[5,6,1,8,4,5]))
    print(llist)
