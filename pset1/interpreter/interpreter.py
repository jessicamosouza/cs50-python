def main():
    expression = input('Expression: ').split(" ")
    print(calculator(expression))


def calculator(expression):
    if expression[1] == '+':
        return float(expression[0]) + float(expression[2])
    elif expression[1] == '-':
        return float(expression[0]) - float(expression[2])
    elif expression[1] == '*':
        return float(expression[0]) * float(expression[2])
    elif expression[1] == '/':
        return float(expression[0]) / float(expression[2])
    else:
        return -1


main()
