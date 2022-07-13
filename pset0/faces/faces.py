def main():
    user_input = input('')
    convert_input = convert(user_input)

    print(convert_input)


def convert(input):
    input_converted = input.replace(':)', '🙂').replace(':(', '🙁')

    return input_converted


main()
