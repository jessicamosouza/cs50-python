def main():
    print(remove_vowels(input('Input: ')))


def remove_vowels(input):
    new_word = ''
    for letter in input:
        if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_word += letter
    return new_word

main()