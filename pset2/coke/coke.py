def main():
    print('Change Owed: ', calc(50, 0))

def calc(amount_due, total_of_coins):
    while amount_due > 0:
        print('Amount due: ', amount_due)
        coin_inserted = int(input('Insert coin: '))
        if coin_inserted != 25 and coin_inserted != 10 and coin_inserted != 5:
            calc(50, 0)
        total_of_coins += coin_inserted
        amount_due -= coin_inserted
    return total_of_coins - 50

main()