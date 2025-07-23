class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        # Edge case - it's ok to have common letters within words.
        # Only word1 and word2 should not be repeated
        wordSet = []
        for char in words:
            wordSet.append(set(char))

        maxLen = 0
        for i in range(len(wordSet)):
            for j in range(i +1, len(wordSet)):
                if not (wordSet[i] & wordSet[j]):
                    maxLen = max(maxLen, len(words[i]) * len(words[j]))
        
        return maxLen

sol = Solution(words = ["abcw","baz","foo","bar","xtfn","abcdef"])
print(sol)
