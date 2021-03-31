n,l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))

def solve(m):
    cnt = 0
    pre = 0
    for i in range(1,n):
        if (a[i] - pre >= m and l - a[i] >= m):
            cnt += 1
            pre = a[i]
    if (cnt >= k):
        return True

#探索の範囲
left = -1
right = l + 1

#条件を満たす最大整数を探す二分探索
while (left <= right):
    mid = (left + right) // 2
    if solve(mid):
        left = mid
    else:
        right = mid
print(left)
