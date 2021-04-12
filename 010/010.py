n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
q = int(input())
b = [list(map(int,input().split())) for _ in range(q)]


for i in range(q):
    ans1 = 0
    ans2 = 0
    for j in range(b[i][0]-1,b[i][1]):
        if a[j][0] == 1:
            ans1 += a[j][1]
        else:
            ans2 += a[j][1]

    print(ans1,ans2)
