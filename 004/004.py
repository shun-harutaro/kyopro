h, w = map(int,input().split())
array = [list(map(int, input().split())) for _ in range(h)]

rows = [0] * h
columns = [0] * w
ans = [[0] * w for _ in range(h)]

for i in range(h):
    row = sum(array[i])
    rows[i] = row

for i in range(w):
    column = 0
    for j in range(h):
        column += array[j][i]
    columns[i] = column

for i in range(h):
    for j in range(w):
        ans[i][j] = rows[i]+columns[j]-array[i][j]

print(ans)
