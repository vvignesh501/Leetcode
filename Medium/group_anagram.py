import collections


class Solution():
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


val = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = Solution().groupAnagrams(val)
print(output)
