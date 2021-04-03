n, m = map(int,input().split()) # nは頂点の数 mは辺の数
graph = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

import queue

def bfs(u):
    q = queue.Queue()
    q.put(u)
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while not q.empty():
        v = q.get()
        for i in graph[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                q.put(i)
    return d

# 0からの各頂点の距離
d = bfs(0)
print(d)
