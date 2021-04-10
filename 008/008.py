s = input()
ss = len(s)

dp = [[0] * 9 for _ in range(ss+1)]
# Dynamic Programming(DP)
dp[0][0] = 1
for i in range(ss):
    for j in range(8):
        dp[i + 1][j] += dp[i][j]
        if s[i] == 'a' and j == 0:
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == 't' and j == 1:
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == 'c' and j == 2:
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == 'o' and j == 3:
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == 'd' and j == 4:
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == 'e' and j == 5:
            dp[i + 1][j + 1] += dp[i][j]
        if s[i] == 'r' and j == 6:
            dp[i + 1][j + 1] += dp[i][j]

    #for j in range(7)

print(dp)
print(dp[ss][7])
