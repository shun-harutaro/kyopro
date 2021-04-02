#https://qiita.com/gogotealove/items/11f9e83218926211083a 1
money = 300
item = (("orange", 100),("apple", 200),("greap", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):
        if((i >> j) & 1): # 順に右にシフトさせ再開bitのチェックを行う
            bag.append(item[j][0]) # フラグが立っていたら bag に果物を詰める
            total += item[j][1]
    if (total <= money):
        print(total, bag)
