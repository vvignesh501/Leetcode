class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:

        letters, digits = [], []
        for log in logs:
            print(log.split(' ', 1))
            splitExceptIdentifier = log.split(' ', 1)[1]
            if splitExceptIdentifier[0].isalpha():
                letters.append(log)
            else:
                digits.append(log)

        letters.sort(key=lambda x: x.split(' ')[0])
        letters.sort(key=lambda x: x.split(' ')[1:])
        print(letters)

        return letters + digits


out = Solution().reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(out)