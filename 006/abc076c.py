import sys

s = list(input())
t = list(input())

length = len(t)
position = len(s) - length

while position >= 0:
    text = s[position:position + length]
    for i in range(length):
        if text[i] == "?":
            text[i] = t[i]
    if text != t:
        position -= 1
    else:
        s[position:position+length] = t
        position = -10

if position != -10:
    print("UNRESTORABLE")
    sys.exit()

for i in range(len(s)):
    if s[i] == "?":
        s[i] = "a"

print("".join(s))
