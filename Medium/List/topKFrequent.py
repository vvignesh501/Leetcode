import collections


class Solution:
    def topKFrequent(self, words, k):
        words.sort()
        d = collections.Counter(words)
        ans = []
        d = d.most_common()
        for each in d:
            if k:
                ans.append(each[0])
                k -= 1
            else:
                break
        return ans


g = Solution()
out = g.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
print(out)
