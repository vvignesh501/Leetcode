n = 1223322
temp = n
new = 0

while temp:
    mod = temp % 10
    # Ones, tens and hundreds digit. Hence multiply by 10
    new = new*10 + mod
    temp = temp // 10

if new == n:
    print("Palindrome")
else:
    print("Not a palindrome")

