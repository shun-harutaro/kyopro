mx = 9999
n = int(input())
c,b,a = sorted(map(int,input().split()))
ans = mx
for i in range(mx):
    if a * i > n:
        break
    for j in range(mx):
        if i + j == mx or a*i+b*j > n:
            break
        if (n-a*i-b*j)%c == 0:
            ans = min(ans, i+j+(n-a*i-b*j)//c)

print(ans)
