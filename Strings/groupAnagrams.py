from collections import defaultdict


def groupAnagrams(words):
    # Write your code here.
    dic = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dic:
            dic[sorted_word].append(word)
        else:
            dic[sorted_word] = [word]
    return [dic.values()]


out = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(out)