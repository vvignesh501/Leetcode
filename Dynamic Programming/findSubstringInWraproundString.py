class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:

        
        dp= [0] * 26
        k = 0

        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1

            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], k)  

        return sum(dp) 

        # Time complexity = O(n)-The for loop runs once for each character in s → O(n)
        # Space complexity = O(1)-Even though we store 26 values, that's constant — it does not scale with input size n


sol = Solution(s = "a")
print(sol)
