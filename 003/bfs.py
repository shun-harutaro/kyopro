n, m = map(int,input().split()) # nは頂点の数 mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

from collections import deque

def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

# 0からの各頂点の距離
d = bfs(0)
print(d)
