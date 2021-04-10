n = int(input())
a = [0] * 100

a[0] = 2
a[1] = 3

for i in range(2,n):
    a[i] = a[i - 1] + a[i - 2]

print(a[n-1])
