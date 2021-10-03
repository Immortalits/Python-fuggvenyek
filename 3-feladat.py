text = input('Írj be egy számot: ')


def convert_to_number(text):
    count = int(text)
    return count


def print_hello(count):
    for i in range(count):
        print(f'{i+1}. Hello!')


print_hello(convert_to_number(text))