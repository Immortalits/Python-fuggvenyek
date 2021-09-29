szam = input('Írj be egy számot: ')


def beszelo():
    if szam.isdigit():
        x = int(szam)
        sorszam = 0
        while x > 0:
            sorszam += 1
            x -= 1
            print(f'{sorszam}. Helló!')


beszelo()
