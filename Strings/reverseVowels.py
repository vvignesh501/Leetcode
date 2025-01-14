class Solution:
    def reverseVowels(self, s: str) -> str:
        st = list(s)
        left = 0
        right = len(s) - 1

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while left < right:
            if st[left] not in vowels:
                left += 1
            elif st[right] not in vowels:
                right -= 1
            else:
                st[right], st[left] = st[left], st[right]
                left += 1
                right -= 1

        return ''.join(st)


out = Solution().reverseVowels("leetcode")
print(out)