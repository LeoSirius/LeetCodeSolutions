def gg():
    i = 0
    while True:
        yield i
        i += 1

g = gg()
for i in g:
    print(i)
    if i == 10:
        g.close()