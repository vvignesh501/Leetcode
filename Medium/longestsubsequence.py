class Solution(object):
    def lengthOfLongestSubstring(self, s):

        n = len(s)
        for i in range(0, 2):
            ii = s[i]
            jj = s[i+1]
            kk = s[i+2]
            if (0 <= ii <= n) and (0 <= jj <= n) and (0 <= kk <= n):
                if ii < jj < kk:
                    stri = "true"
                else:
                    stri = "false"
            else:
                stri = "false"

        return stri


s = [1,2,3,4,5]
longest_subseq = Solution().lengthOfLongestSubstring(s)
print(longest_subseq)