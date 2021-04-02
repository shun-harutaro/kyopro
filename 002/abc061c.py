s = input()

n = len(s) - 1
total = 0
for bit in range(1 << n):
    siki = s[0]
    for i in range(n):
        if bit & (1 << i):
            siki += '+'
        siki += s[i+1]
    total += eval(siki)
print(total)

