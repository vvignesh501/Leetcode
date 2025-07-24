class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True

        # # Worst solution
        # hashRansom = {}
        # hashMagazine = {}

        # for char in ransomNote:
        #     if char in hashRansom:
        #         hashRansom[char] += 1
        #     else:
        #         hashRansom[char] = 1

        # for char in magazine:
        #     if char in hashMagazine:
        #         hashMagazine[char] += 1
        #     else:
        #         hashMagazine[char] = 1

        
        # for char, idx in hashRansom.items():
        #     if hashMagazine.get(char, 0) < idx:
        #         return False
        # return True

sol = Solution(ransomNote = "a", magazine = "b")
print(sol)
