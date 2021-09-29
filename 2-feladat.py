x = [
    'Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László',
    'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista'
]


def pistazo():
    y = 0
    for p in x:
        if p == 'Pista':
            y += 1
    return y


print(pistazo())
