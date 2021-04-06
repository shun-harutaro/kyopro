t = int(input())
for t in range(t):
    s = input()
    count = 0
    position = 0
    while position < len(s) - 4:
        if s[position:position + 5] == "tokyo" or s[position:position + 5] == "kyoto":
            count += 1
            position += 5
        else:
            position += 1
    print(count)
