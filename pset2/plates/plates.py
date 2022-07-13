def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # max of 6 characters (letters or numbers) and a min of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # numbers cannot be used in the middle of a plate. AAA222 = valid; AAA22A = invalid;
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    # and the first number cannot be 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            break
        i += 1

    # no periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False

    return True


main()
