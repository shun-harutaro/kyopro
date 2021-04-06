charge = 1000 - int(input())

count_coin = 0

coin_kind = [1, 5, 10, 50, 100, 500]

for i in range(1,7):
    t = charge // coin_kind[-i]
    charge -= t * coin_kind[-i]
    count_coin += t

print(count_coin)
