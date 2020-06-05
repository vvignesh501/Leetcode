class Solution():
    def removeNthFromEnd(self, list : 'Listnode', n: 'index') -> 'ListNode':
        del list[-n]
        print(list)


listnode = [1, 2, 3, 4, 5]
n = 2
Solution().removeNthFromEnd(listnode, n)
