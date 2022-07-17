taqueria_menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0
    while True:
        try:
            total += get_itens()
        except KeyError:
            pass
        except EOFError:
            print("\n")
            break
        else:
            print(f"Total: ${total:.2f}")



def get_itens():
    item = input("Item: ").title()
    if item in taqueria_menu:
        return taqueria_menu.get(item)
    else:
        raise KeyError

main()