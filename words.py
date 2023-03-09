def print_upper_words(words):

    for word in words:
        print(word.upper())

print_upper_words(['magnetic', 'electromagnetic', 'difuser'])

def print_upper_words_e(words):

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

print_upper_words_e(['magnetic', 'electromagnetic', 'difuser', 'elon'])


def print_upper_words_specific(words, must_start_with):

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words_specific(['magnetic', 'electromagnetic', 'difuser', 'elon'], must_start_with=['m', 'e'])
