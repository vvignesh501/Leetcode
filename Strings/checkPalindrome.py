string = 'liri'
l, r = 0, len(string) - 1

while l <= r:
    if string[l] == string[r]:
        l += 1
        r -= 1
    else:
        print("Not a palindrome")
        break

# print(''.join(list(reversed(string))))
print("Its a palindrome")
