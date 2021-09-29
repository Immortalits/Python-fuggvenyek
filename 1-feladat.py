def fuggveny(start, finish, oszthato, nem_oszthato):
    x = []
    for p in range(start, finish):
        if p % oszthato == 0:
            x.append(p)
        for p in x:
            if p % nem_oszthato == 0:
                x.remove(p)
    print(x)


fuggveny(2000, 3200, 7, 5)