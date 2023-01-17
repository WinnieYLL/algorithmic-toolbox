# Import math library
import math


def change(money):
    MinNumCoins = []
    coins = [1, 3, 4]
    for m in range(money+1):
        MinNumCoins.append(float('inf'))
    MinNumCoins[0] = 0

    for m in range(money+1):
        for i in coins:
            if (m >= i):
                NumCoins = MinNumCoins[m - i] + 1
                if (NumCoins < MinNumCoins[m]):
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
