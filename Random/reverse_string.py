class Solution():
    def reverseString(self, val):
        
        out = val[::-1]
        for i in range(len(out)):
            val[i] = out[i]
        return val
    
val = ["h","e","l","l","o"]
out = Solution().reverseString(val)
print(out)