class Solution:

    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(index, path):
            # Base case: if we're at the end and the sequence is valid
            if index == len(num):
                return len(path) >= 3

            for i in range(index + 1, len(num) + 1):
                curr_str = num[index:i]
                # Skip numbers with leading zeros
                if len(curr_str) > 1 and curr_str[0] == '0':
                    break

                curr_num = int(curr_str)

                if len(path) >= 2:
                    if curr_num != path[-1] + path[-2]:
                        continue

                path.append(curr_num)
                if backtrack(i, path):
                    return True
                path.pop()  # Backtrack

            return False

        return backtrack(0, [])

sol = Solution("112358")
print(sol)
