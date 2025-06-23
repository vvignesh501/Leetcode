class Solution:
    def addBinary(self, a: str, b: str) -> str:

      # First convert the binary to a list and pop the element
      a = list(a)
      b = list(b)

      # Create a new list to add two binaries
      res = ''
      carry = 0

      while a or b or carry:

        if a:
          carry += int(a.pop())
        
        if b:
          carry += int(b.pop())

        # Modulo gives the last digit after addition
        res += str(carry %2)

        # Divide gives the first digit after addition
        # Perform modulo first then divide
        carry //=2
      
      return res[::-1]

add = Solution().addBinary(a='11', b='1')
print(add)
