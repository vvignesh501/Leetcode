# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(None)  # initilize the first node of your resulting spliced list
        l3 = head  # create a variable that marks the beginnning of your LinkedList. l3 is simply the head of your spliced linked list
        while l1 and l2:  # while l1 and l2 are not None, the iteration will proceed
            if l1.val < l2.val:
                head.next = l1
            else:
                head.next = l2
        if l1.val < l2.val:  # if the l1 value was smaller, than we iterate through to the next node of l1
            l1 = l1.next
        else:
            l2 = l2.next  # otherwise we iterate to the next node of l2
        head = head.next  # traverse to the next node in our spliced list
        head.next = l1 if l1 else l2  # This line is explained below!
        return l3.next  # The traversal of the list begins from the second node hence "l3.next" (not from the first since the first node is thehead and the head is None)


g = Solution()
out = g.mergeTwoLists([4,2, 1], [1,3,4])
print(out)