x = [
    'Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter',
    'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs',
    'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás',
    'Xtra'
]


def abc(y):
    y = sorted(y)
    return y


rend = abc(x)
hossz = len(rend)

elso_fele = []
masodik_fele = []

for p in range(len(rend)):
    if len(rend) % 2 == 0:
        if p < len(rend) / 2:
            elso_fele.append(rend[p])
        if p >= len(rend) / 2:
            masodik_fele.append(rend[p])
    else:
        if p < int((len(rend) + 1) / 2):
            elso_fele.append(rend[p])
        if p > int(len(rend) / 2):
            masodik_fele.append(rend[p])

print('1. csoport:')
for q in elso_fele:
    print(q)

print('2. csoport:')
for f in masodik_fele:
    print(f)
# print(f'1. csoport: {elso_fele}')
# print(f'2. csoport: {masodik_fele}')