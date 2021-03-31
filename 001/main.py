n,l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))

def solve(m):
    cnt = 0
    pre = 0
    for i in range(1,n):
        if (a[i] - pre >= m and l-a[i] >= m):
            cnt += 1
            pre = a[i]
    if (cnt >= k):
        return True
    else:
        return False

#二分探索
left = -1
right = l + 1
while (right - left > 1):
    mid = left + (right - left) // 2
    if (solve(mid) == False):
        right = mid
    else:
        left = mid;
print(left)
