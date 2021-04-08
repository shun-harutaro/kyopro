n = int(input()) #クラス数
a = list(map(int, input().split())) # 各教室のレーティング
q = int(input()) # 人数
b = [0] * q # 各生徒のレーティング 
for i in range(q):
    b[i] = int(input())

# 1,ソートする
a.sort()

# 2, 二分探索(binary_serch)
# 探索範囲
left = 0
right = q + 1

for i in range(q):
    diff1 = 0
    while abs(right - left) > 1:
        mid = (left + right) // 2
        if a[mid] >= b[i]:
            left = mid
            diff1 = mid
        else:
            right = mid
    print(a[diff1])
