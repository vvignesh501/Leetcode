class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # You can minus t - s
        # But you can convert to ord and then minus
        # Eg - "abcde" - "abcd" = 495-394 = e
        sum_s, sum_t = 0, 0
        for c in s:
            sum_s += ord(c)
        
        for c in t:
            sum_t += ord(c)
        
        print(sum_s, sum_t)
        return chr(sum_t - sum_s)

sol = Solution(s="abcd", t="abcd")
print(sol)
