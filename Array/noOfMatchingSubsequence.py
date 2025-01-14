from collections import defaultdict


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_dict = defaultdict(list)
        res = 0

        # create a dictionary as key & val from i/p words as a: [a, acd, ace] b:[bb]
        # traverse through each elem in string and if a remove the a from the vals in dict.
        # Eg - Remove a if a is found. cd, ce is pending. So the dict is changed as c:[cd, ce]
        # if all the values are removed in dict, increment count to + 1.
        for word in words:
            word_dict[word[0]].append(word)

        for s in S:
            if s in word_dict:
                cur_words = word_dict.pop(s)
                print(cur_words)
                for word in cur_words:
                    if len(word) == 1:
                        res += 1
                    else:
                        word_dict[word[1]].append(word[1:])
        return res


out = Solution().numMatchingSubseq("abcde", ["a","bb","acd","ace"])
print(out)