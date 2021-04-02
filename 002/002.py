n = int(input())

def judge(s):
    dep = 0
    for i in range(len(s)):
        if s[i] == '(':
            dep += 1
        if s[i] == ')':
            dep -= 1
        if (dep < 0):
            return False
    if (dep == 0):
        return True
    return False

for i in range(1 << n): # 1 << n == 2 ** n
    kakko = ""
    for j in reversed(range(0,n)):
        # memo: (i & (i<<j))=0 というのはiのjビット目(2^jの位)が0であるための条件
        if (i & (1 << j)) == 0:
            kakko += "("
        else:
            kakko += ")"
    if judge(kakko):
        print(kakko)
