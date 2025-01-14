class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        new_string = ""
        # while loop for a stack

        for char in s:
            if char == "[":
                continue

            elif char not in ["[", "]"]:
                stack.append(char)

            elif char in "]":
                substring = ""
                while stack:
                    new_char = stack.pop()
                    if new_char.isdigit():
                        substring = int(new_char) * substring
                    else:
                        substring = new_char + substring

                new_string += substring
            else:
                new_string += char

        return new_string


out = Solution().decodeString("2[abc]3[cd]ef")
print(out)
