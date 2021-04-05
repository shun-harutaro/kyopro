#===標準入力と使用するデータの整理===#
r, c = map(int,input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sx, sy, gx, gy = [i-1 for i in [sx, sy, gx, gy]] # 座標をindexに修正
maiz = []
for _ in range(r):
    line = list(input())
    maiz.append(line)

#=== 幅優先探索 開始 ===#
queue = [[sx, sy]] # スタート地点をキューに入れる
maiz[sy][sx] = 0 # 手数0からスタート
visited = [[False] * c for _ in range(r)] # 訪問したかどうかをメモする
while queue:
    x, y = queue.pop(0)
    visited[y][x] = True # 訪問済みにする
    hjkl = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]] # 次に訪れる場所 左上右下
    for dx, dy in hjkl:
        if (maiz[dy][dx] == '.') and (visited[dy][dx] is False):
            # 進行可能でまだ訪問していなければキューに入れてかかった手数を記録する
            queue.append([dx, dy])
            maiz[dy][dx] = maiz[y][x] + 1

print(maiz[gy][gx]) # ゴール地点に記録された手数を参照
