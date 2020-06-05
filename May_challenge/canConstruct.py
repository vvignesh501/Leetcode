from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(Counter(ransomNote))
        print(Counter(magazine))
        print(Counter(ransomNote) - Counter(magazine))
        return (Counter(ransomNote) - Counter(magazine)) == {}




g = Solution()
out = g.canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
print(out)