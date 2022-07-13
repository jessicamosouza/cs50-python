def main():
    mass = int(input('m: '))
    energy = emc(mass)

    print(f"E: {energy}")


def emc(m):
    return m * pow(300000000, 2)


main()
