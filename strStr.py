class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            out = haystack.index(needle)
        return out


if __name__ == '__main__':
    out = Solution()
    result = out.strStr("hello", "ll")
    print(result)