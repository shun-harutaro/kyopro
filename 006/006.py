s = input()
k = int(input())
ss = len(s)
nex = [[0] * 26 for _ in range(ss)]

n2a = lambda c: chr(c+97)
a2n = lambda c: ord(c) - ord('a')

# step2 前計算
for i in range(26):
    nex[ss-1][i] = ss
for i in reversed(range(ss-1)):
    for j in range(26):
        if a2n(s[i]) - a2n('a') == j:
            nex[i][j] = i
        else:
            nex[i][j] = nex[i + 1][j]
print(nex)
 
# step3 一文字ずつ貪欲法で決める
answer = ""
current_pos = 0
for i in range(k):
    for j in range(26):
        nex_pos = nex[current_pos][j]
        max_possible_length = ss - nex_pos - 1 + i
        if max_possible_length >= k:
            answer += n2a(a2n('a') + j)
            current_pos = nex_pos + 1
            break

print(answer)
