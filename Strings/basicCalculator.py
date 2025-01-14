class Solution:
    def calculate(self, s: str) -> int:

        num = 0
        stack = [1]
        sign = 1
        output = 0
        s += "+"

        for c in s:

            # Multiply by 10 to receive the whole number
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == "+":
                output += num * sign
                sign = 1
                num = 0

            elif c == "-":
                output += num * sign
                sign = -1
                num = 0

            elif c == "(":
                stack.append(sign * stack[-1])
                sign = 1

            elif c == ")":
                output += num * sign

                # Pop the stack values appended under "("
                # When it's a sign you have to multiply
                output *= stack.pop()

                # make the number back to 0
                num = 0

        return output


out = Solution().calculate("1-(     -2)")
print(out)