def longestCommonSubsequence(str1, str2):
    # Write your code here.

    dp = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + [str2[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[-1][-1]


out = longestCommonSubsequence("abcde", "ace")
print(out)
