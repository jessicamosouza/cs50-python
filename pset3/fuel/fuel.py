def main():
    fuel = calc_fuel()
    if fuel >= 0.99:
        print("F")
    elif fuel <= 0.1:
        print("E")
    else:
        print(f"{round(fuel*100)}%")


def get_fraction():
    fraction = input("Fraction: ").split('/')
    if int(fraction[0]) > int(fraction[1]):
        raise Exception()
    return int(fraction[0]) / int(fraction[1])

def calc_fuel():
    while True:
        try:
            fuel = get_fraction()
        except (Exception, ValueError, ZeroDivisionError):
            pass
        else:
            return fuel

main()
