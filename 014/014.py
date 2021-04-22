n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

aa = sorted(a)
bb = sorted(b)

answer = 0
for i in range(n):
    ans += abs(aa[i] - bb[i])
print(ans)
