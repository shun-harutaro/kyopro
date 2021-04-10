#count_dp = [float('inf')] * 100001 # 1~100000における最小回数の記録

n = int(input())
a = [ 1, 6, 10, 50, 234 ]
count_dp = [float('inf')] * (n+1)

count_dp[0] = 0

for i in range(1,n+1):
    for j in range(5):
        if i < a[j]:
            break
        count_dp[i] = min(count_dp[i - a[j]] + 1, count_dp[i])

print(count_dp[n])
print(count_dp)
