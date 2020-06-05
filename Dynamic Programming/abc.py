def myGenerator(stop):
    z = 0
    while z < stop:
        yield z * 2
        z += 1

g = myGenerator(4)

for n in g:
    print(n, end=' ')