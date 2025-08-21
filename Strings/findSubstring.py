class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hashMap = Counter(words)
        word_len, word_num = len(words[0]), len(words)
        total_word_len = word_len*word_num
        res = []
        
        # Slide the window until until the len of the words i.e check 0-6, 1-7, 2-8,...13-18
        for i in range(len(s)-total_word_len+1):
            # Create another hashMap called seen and if all words in seen  
            # matches to hashMap then it's matching
            seen = defaultdict(int)
            
            for j in range(i, i+total_word_len, word_len):
                cur_word = s[j:j+word_len]
                
                if cur_word in hashMap:
                    seen[cur_word] += 1
                    
                    # If count of seen is greater than count of hashMap, then break
                    if seen[cur_word]>hashMap[cur_word]:
                        break
                        
                # if cur_word is not a part in hashMap, then the entire sequence 
                # is not possible either, we break.
                else:
                    break
                    
            # if seen == hashMap, we append its starting index
            if seen==hashMap:
                res.append(i)
        return res

sol = Solution(s = "barfoothefoobarman", words = ["foo","bar"])
print(sol)
