s = input()
k = int(input())
ss = len(s)
nex = [[] * 26 for _ in range(ss)]

# step2 前計算
for i in range(26):
    nex[ss-1][i] = ss
for i in reversed(range(ss-1)):
    for j in range(range(26)):

    
