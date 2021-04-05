def getdist(start):
    dist = [-1] * n
    dist[start] = 0
    # BFSにより、最短距離を計算
    #for i in range(n-1):
        #dist[i] = INF
    queue = []
    queue.append(start)

    while queue:
        pos = queue.pop()
        for to in g[pos]:
            if dist[to] == -1:
                dist[to] = dist[pos] + 1
                queue.append(to)
    print(dist)
    return dist

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

print(g)
   
# step2 頂点１からの最短距離を求める
# maxid1: 頂点１から最も離れている（最短距離が長い）頂点
dist = getdist(1)
maxn1 = max(dist)
maxid1 = dist.index(maxn1)

# step3 頂点maxid1 からの最短距離を求める
# maxn2: 木の直径（最短距離の最大値）
dist = getdist(maxid1)
maxn2 = max(dist)

# step4 出力
print(maxn2 + 1)
