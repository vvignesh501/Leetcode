class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        temp = x
        reversed_num = 0

        while temp != 0:
            rem = temp % 10
            reversed_num = reversed_num * 10 + rem
            temp = temp // 10

        return reversed_num == x



sol = Solution().isPalindrom(123)
