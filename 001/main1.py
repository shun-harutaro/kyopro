n,l = map(int,input().split())
k = int(input())
a = list(map(int,input().split()))

l1 = [0]*(n+1)
l1[0] = a[0]
for i in range(1,n):
    l1[i] = a[i] - a[i-1]
l1[n] = l - a[n-1]
print(l1)
