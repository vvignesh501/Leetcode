def generateDocument(characters, document):
    # Write your code here.

    dic = {}
    for char in characters:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    for i in document:
        if i in dic and dic[i] != 0:
            dic[i] -= 1
        elif i not in dic:
            return False
    return True


out = generateDocument(characters="aheaolabbhb", document="hello")
print(out)
