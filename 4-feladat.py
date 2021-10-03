import math

sugar = input('Add meg a kör sugarát: ')


def convert_to_number(sugar):
    r = int(sugar)
    return r


def kerulet(r):
    kerulet = 2 * math.pi * convert_to_number(r)
    return kerulet


def terulet(r):
    terulet = math.pi * convert_to_number(r)**2
    return terulet


print(kerulet(sugar))
print(terulet(sugar))