from pyclbr import Function


days = ['Mon', 'Tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words: list, func: Function):
    for word in words:
        print(func(word))


# def convert_to_capital(word):
#     return word.capitalize()

def convert_to_capital(word): return word.capitalize()


change_words(days, convert_to_capital)
