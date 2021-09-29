def func(start, finish, oszthato, nem_oszthato):
    x = []
    for p in range(start, finish):
        if p % oszthato == 0:
            x.append(p)
        for p in x:
            if p % nem_oszthato == 0:
                x.remove(p)
    print(x)


func(start=2000, finish=3200, oszthato=7, nem_oszthato=5)
