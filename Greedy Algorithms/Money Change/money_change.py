# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    penny = 1
    nickel = 5
    dime = 10
    coins = 0
    while money>0:
        if money >= dime:
            coins=coins+1
            money=money-dime
        if money < dime and money >= nickel:
            coins=coins+1
            money=money-nickel
        if money < nickel and money >= penny:
            coins=coins+1
            money = money-1
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
