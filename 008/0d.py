# https://qiita.com/bplain2/items/8e5bb79e4642368fe275
# 0次元DP

a = list(map(int,input().split()))

ma = 0
for i in range(len(a)):
    ma = max(ma, a[i])

print(ma)
