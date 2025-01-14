import itertools

class Solution:
    def letterCombinations(self, digits: str):
        letter = []

        if not digits:
            return letter

        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for i in digits:
            letter.append(letters[i])
        letter_combinations = list("".join(a) for a in itertools.product(*letter))
        return letter_combinations


out = Solution().letterCombinations("23")
print(out)